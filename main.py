import os
import cv2
import numpy as np
import shutil
import json
import datetime
from modules import (
    config,
    image_processor,
    generate_files_canny,
    generate_files_binary,
    generate_files_thinning,
    detect_person_and_get_roi,
    detect_face_and_get_roi,
    run_photo_booth,
    run_zed_capture,
    generate_sketch,
    generate_gemini_sketch
)

class SketchApp:
    def __init__(self):
        print(">> 심플 G-코드 변환기 (AI 스케치 통합 버전) 시작")
        os.makedirs(config.GENERAL_INPUT_DIR, exist_ok=True)
        os.makedirs(config.CHARACTERS_DIR, exist_ok=True)
        config.initialize_session()
        self.photo_counter = 1
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.gemini_prompt = None
        self.character_image = None
        
        # 프롬프트 설정 파일 경로
        self.prompts_file = os.path.join(config.BASE_DIR, "config", "gemini_prompts.json")
        self.char_prompts_file = os.path.join(config.BASE_DIR, "config", "gemini_character_prompts.json")
        self.prompts_dict = self.load_prompts()
        self.char_prompts_dict = self.load_character_prompts()

    def load_prompts(self):
        """JSON 파일에서 일반 프롬프트 목록을 로드합니다."""
        default_prompts = {
            "1. 세선화 최적화 (기본)": "A high-quality, pure black line art caricature based on the provided image. The entire drawing is rendered exclusively with lines of exactly the same thickness (uniform line weight, minimal width) using only solid black ink. DO NOT FILL ANY AREAS with solid color. Draw everything, including eyes and pupils, as hollow outlines only. Ensure there are no solid black regions or shading. The lines are precise and appear machine-drawn for direct path tracing.",
            "2. 정밀한 얼굴 캐리커처": "A highly detailed black ink line art focusing on facial features and expressions. Pure black lines on a clean white background. Strictly NO SOLID FILLS. Eyes and pupils must be rendered as clean, hollow circular outlines with no solid color inside. The drawing must consist entirely of empty closed loops and paths for precise portrait plotting.",
            "3. 미니멀리스트 (최소한의 선)": "An extreme minimalist line drawing using the absolute minimum number of continuous black lines to represent the person's character. Strictly no solid fills or shading. Represent eyes and pupils as simple hollow shapes without filling them. Only pure black outlines on a white background. Very clean for fast plotting.",
            "4. 굵은 코믹스 외곽선": "Bold and strong black outlines, comic book style line art. Use only outlines to define shapes. Do not use solid fills for shadows, hair, or features. Eyes and pupils must be rendered as hollow line drawings with no solid fill. No solid black regions. High contrast but composed entirely of empty paths."
        }
        
        return self._load_json_prompts(self.prompts_file, default_prompts)

    def load_character_prompts(self):
        """JSON 파일에서 캐릭터 동반 전용 프롬프트 목록을 로드합니다."""
        default_char_prompts = {
            "1. 어깨 위의 파트너": "A pure black line art caricature of the person from the first image with the character from the second image sitting naturally on their shoulder. They are in the same scene, interacting. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients. Hollow eyes. Machine-drawn style for plotting.",
            "2. 나란히 서 있는 친구": "A pure black line art caricature of the person from the first image standing side-by-side with the character from the second image as friends. Draw them interacting naturally. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients. Hollow eyes.",
            "3. 머리 위의 요정": "A pure black line art caricature of the person from the first image with the small character from the second image sitting or floating above their head like a fairy. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients.",
            "4. 함께 손을 흔드는 모습": "A pure black line art caricature of the person from the first image and the character from the second image standing together and waving their hands at the viewer. Both are in the same line art style, rendered exclusively with lines of exactly the same thickness using solid black ink."
        }
        
        return self._load_json_prompts(self.char_prompts_file, default_char_prompts)

    def _load_json_prompts(self, file_path, default_data):
        if not os.path.exists(file_path):
            try:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, indent=4, ensure_ascii=False)
                print(f"[설정] 기본 프롬프트 파일이 생성되었습니다: {file_path}")
            except Exception as e:
                print(f"[경고] 프롬프트 파일 생성 실패: {e}")
            return default_data
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if data else default_data
        except Exception as e:
            print(f"[경고] 프롬프트 파일을 읽는 중 오류 발생: {e}")
            return default_data

    def check_gemini_config(self, is_character_mode=False):
        """Gemini 사용 전 API 키와 프롬프트를 확인 및 설정합니다."""
        if not self.gemini_api_key:
            print("\n[설정] Gemini API 키가 환경변수에 없습니다.")
            self.gemini_api_key = input("API 키를 입력해주세요 (Enter로 건너뛰기 가능하나 기능 제한됨): ").strip()
            if not self.gemini_api_key:
                print("[경고] API 키가 없어 Gemini 기능을 사용할 수 없습니다.")
                return False
        
        # 모드에 따른 프롬프트 딕셔너리 선택
        current_prompts = self.char_prompts_dict if is_character_mode else self.prompts_dict
        prompt_keys = list(current_prompts.keys())
        mode_name = "캐릭터 동반" if is_character_mode else "Gemini 스타일"

        print("\n" + "-"*40)
        print(f" [{mode_name} 선택]")
        print("-"*40)
        print(" 0. 모든 프롬프트 순차 실행 (Batch Mode)")
        for i, key in enumerate(prompt_keys, 1):
            print(f" {i}. {key}")
        print(f" {len(prompt_keys) + 1}. 사용자 직접 입력")
        print("-"*40)
        
        try:
            p_input = input(f"선택 (0~{len(prompt_keys) + 1}, 기본값 1): ").strip()
            if p_input == '0':
                self.gemini_prompt = current_prompts # 딕셔너리 전체 전달
                print(">> [배치 모드] 모든 프롬프트를 순서대로 실행합니다.")
            elif not p_input:
                self.gemini_prompt = current_prompts[prompt_keys[0]]
            else:
                p_choice = int(p_input)
                if 1 <= p_choice <= len(prompt_keys):
                    selected_key = prompt_keys[p_choice - 1]
                    self.gemini_prompt = current_prompts[selected_key]
                    print(f">> '{selected_key}' 스타일이 적용되었습니다.")
                elif p_choice == len(prompt_keys) + 1:
                    self.gemini_prompt = input("프롬프트를 직접 입력하세요: ").strip()
                else:
                    self.gemini_prompt = current_prompts[prompt_keys[0]]
        except (ValueError, IndexError):
            self.gemini_prompt = current_prompts[prompt_keys[0]]
            
        return True

    def select_character_image(self):
        """합성할 캐릭터 이미지를 폴더에서 선택합니다."""
        if not os.path.exists(config.CHARACTERS_DIR):
            os.makedirs(config.CHARACTERS_DIR, exist_ok=True)
            
        files = [f for f in os.listdir(config.CHARACTERS_DIR) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if not files:
            print(f"\n[안내] '{config.CHARACTERS_DIR}' 폴더에 캐릭터 이미지가 없습니다.")
            print("합성 없이 사용자 사진만으로 진행합니다.")
            return None

        print("\n" + "-"*40)
        print(" [동반할 캐릭터 선택]")
        print("-"*40)
        for i, filename in enumerate(files, 1):
            print(f" {i}. {filename}")
        print("-"*40)

        try:
            choice = input(f"선택 (1~{len(files)}, 기본값 1): ").strip()
            if not choice:
                idx = 0
            else:
                idx = int(choice) - 1
            
            if 0 <= idx < len(files):
                selected_file = os.path.join(config.CHARACTERS_DIR, files[idx])
                img_array = np.fromfile(selected_file, np.uint8)
                char_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                if char_img is not None:
                    print(f">> '{files[idx]}' 캐릭터가 선택되었습니다.")
                    return char_img
                else:
                    print(f"[오류] 캐릭터 이미지를 불러올 수 없습니다: {files[idx]}")
        except (ValueError, IndexError):
            print("[알림] 잘못된 입력입니다. 첫 번째 캐릭터로 진행합니다.")
            if files:
                selected_file = os.path.join(config.CHARACTERS_DIR, files[0])
                img_array = np.fromfile(selected_file, np.uint8)
                return cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        return None

    def run(self):
        while True:
            choice = self.show_main_menu()
            if choice == 'Q':
                print("프로그램을 종료합니다.")
                break
            
            mode_map = {
                '1': ('AI_ANIME', 'ZED'),
                '2': ('AI_ANIME', 'WEBCAM'),
                '3': ('AI_ANIME', 'FILE'),
                '4': ('GEMINI', 'ZED'),
                '5': ('GEMINI', 'WEBCAM'),
                '6': ('GEMINI', 'FILE'),
                '7': ('GEMINI_CHAR', 'ZED'),
                '8': ('GEMINI_CHAR', 'WEBCAM'),
                '9': ('GEMINI_CHAR', 'FILE')
            }
            
            if choice not in mode_map:
                print("[알림] 잘못된 선택입니다.")
                continue
                
            sketch_type, input_type = mode_map[choice]
            
            # 캐릭터 이미지 및 프롬프트 설정 초기화
            self.character_image = None
            self.gemini_prompt = None
            
            if sketch_type == 'GEMINI':
                if not self.check_gemini_config(is_character_mode=False):
                    continue
            elif sketch_type == 'GEMINI_CHAR':
                if not self.check_gemini_config(is_character_mode=True):
                    continue
                self.character_image = self.select_character_image()
                if self.character_image is None:
                    print("[알림] 캐릭터를 선택하지 않아 일반 모드로 전환하거나 취소합니다.")
                    continue
            
            input_data = self.get_input(input_type)
            if input_data is None:
                continue
            
            input_path, base_filename = input_data
            processed_image, intermediate_dir, output_dir = self.preprocess(input_path, base_filename)
            if processed_image is None:
                continue

            self.process_and_save(processed_image, sketch_type, base_filename, intermediate_dir, output_dir)
            
            self.photo_counter += 1
            print("-" * 30)

    def show_main_menu(self):
        print("\n" + "="*50)
        print(" [메인 메뉴] 작업 방식을 선택하세요")
        print("="*50)
        print(" 1. Informative-Drawing AI (Anime) + ZED 카메라")
        print(" 2. Informative-Drawing AI (Anime) + 일반 웹캠")
        print(" 3. Informative-Drawing AI (Anime) + 파일 불러오기")
        print("-" * 50)
        print(" 4. Gemini AI 고품질 스케치 + ZED 카메라")
        print(" 5. Gemini AI 고품질 스케치 + 일반 웹캠")
        print(" 6. Gemini AI 고품질 스케치 + 파일 불러오기")
        print("-" * 50)
        print(" 7. Gemini AI 캐릭터 동반 스케치 + ZED 카메라")
        print(" 8. Gemini AI 캐릭터 동반 스케치 + 일반 웹캠")
        print(" 9. Gemini AI 캐릭터 동반 스케치 + 파일 불러오기")
        print("-" * 50)
        print(" Q. 프로그램 종료")
        print("="*50)
        return input("선택 (1~9 또는 Q): ").strip().upper()

    def get_input(self, input_type):
        photo_specific_name = f"{self.photo_counter}_capture"
        input_dir, _, _ = config.setup_photo_paths(photo_specific_name)

        captured_path = None
        base_name = "photo"

        if input_type == 'ZED':
            print("\n>> ZED 카메라 실행 (SPACE: 촬영, ESC: 취소)")
            captured_path = run_zed_capture(save_dir=input_dir)
            base_name = "zed"

        elif input_type == 'WEBCAM':
            print("\n>> 포토부스 실행 (스페이스바: 촬영, ESC: 취소)")
            captured_path = run_photo_booth(save_dir=input_dir)
            base_name = "webcam"

        elif input_type == 'FILE':
            files = [f for f in os.listdir(config.GENERAL_INPUT_DIR) if os.path.isfile(os.path.join(config.GENERAL_INPUT_DIR, f))]
            if not files:
                print(f"[알림] '{config.GENERAL_INPUT_DIR}' 폴더에 이미지가 없습니다.")
                return None
            
            print(f"\n목록: {', '.join(files)}")
            filename = input("파일명 입력: ").strip().strip('"')
            src_path = os.path.join(config.GENERAL_INPUT_DIR, filename)
            
            if not os.path.exists(src_path):
                print(f"[오류] 파일이 없습니다: {src_path}")
                return None
            
            dest_path = os.path.join(input_dir, filename)
            shutil.copy(src_path, dest_path)
            return dest_path, os.path.splitext(filename)[0]

        if captured_path:
            raw_save_path = os.path.join(config.GENERAL_INPUT_DIR, os.path.basename(captured_path))
            try:
                shutil.copy(captured_path, raw_save_path)
                print(f"[자동 저장] 원본 사진이 '{config.GENERAL_INPUT_DIR}'에 저장되었습니다.")
            except Exception as e:
                print(f"[경고] data/raw 복사 실패: {e}")
            return captured_path, base_name
        
        return None

    def preprocess(self, input_path, base_filename):
        photo_specific_name = f"{self.photo_counter}_capture"
        _, intermediate_dir, output_dir = config.setup_photo_paths(photo_specific_name)

        img_array = np.fromfile(input_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if image is None:
            print("[오류] 이미지를 로드할 수 없습니다.")
            return None, None, None

        person_roi = detect_person_and_get_roi(image)
        cropped = image[person_roi[1]:person_roi[1]+person_roi[3], person_roi[0]:person_roi[0]+person_roi[2]] if person_roi else image
        
        face_roi = detect_face_and_get_roi(cropped)
        if face_roi:
            cropped = cropped[face_roi[1]:face_roi[3], face_roi[0]:face_roi[2]]

        preprocessed = image_processor(cropped)
        if preprocessed is None:
            preprocessed = cropped

        cv2.imencode(".jpg", preprocessed)[1].tofile(os.path.join(intermediate_dir, "preprocessed.jpg"))
        return preprocessed, intermediate_dir, output_dir

    def process_and_save(self, image, sketch_type, base_filename, intermediate_dir, output_dir):
        if (sketch_type == 'GEMINI' or sketch_type == 'GEMINI_CHAR') and isinstance(self.gemini_prompt, dict):
            print(f"\n>> [일괄 처리 시작] 총 {len(self.gemini_prompt)}개의 스타일을 적용합니다.")
            for i, (style_name, prompt_text) in enumerate(self.gemini_prompt.items(), 1):
                safe_style_name = "".join([c if c.isalnum() else "_" for c in style_name])
                current_base = f"{base_filename}_{safe_style_name}"
                print(f"\n[{i}/{len(self.gemini_prompt)}] 스타일 적용 중: {style_name}")
                self._single_process_and_save(image, sketch_type, prompt_text, current_base, intermediate_dir, output_dir)
        else:
            self._single_process_and_save(image, sketch_type, self.gemini_prompt, base_filename, intermediate_dir, output_dir)

    def _single_process_and_save(self, image, sketch_type, prompt, base_filename, intermediate_dir, output_dir):
        if sketch_type == 'AI_ANIME':
            sketch = generate_sketch(image)
            threshold_val = 220
            suffix = "anime"
        else: # GEMINI or GEMINI_CHAR
            sketch = generate_gemini_sketch(
                image, 
                api_key=self.gemini_api_key, 
                prompt=prompt,
                character_image_bgr=self.character_image
            )
            threshold_val = 240
            suffix = "gemini"

        if sketch is None:
            print(f"[오류] '{base_filename}' 스케치 생성 실패")
            return

        output_base = f"{base_filename}_{suffix}"
        cv2.imencode(".png", sketch)[1].tofile(os.path.join(intermediate_dir, f"{output_base}.png"))

        if len(sketch.shape) == 3:
            sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(sketch, threshold_val, 255, cv2.THRESH_BINARY)
        
        nc_path = os.path.join(output_dir, f"{output_base}.nc")
        svg_path = os.path.join(output_dir, f"{output_base}.svg")
        generate_files_thinning(binary, nc_path, svg_path)
        print(f">> 완료: {output_base}.nc")

if __name__ == "__main__":
    app = SketchApp()
    app.run()
