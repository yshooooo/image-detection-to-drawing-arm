import os
import cv2
import numpy as np
import shutil
import json
import datetime
from concurrent.futures import ThreadPoolExecutor
from modules import (
    config,
    image_processor,
    generate_files_canny,
    generate_files_binary,
    generate_files_thinning,
    generate_sketch,
    generate_gemini_sketch,
    CameraCapture,
    GUIViewer,
    HumanCropper
)

class SketchApp:
    def __init__(self):
        # 경로 설정
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.prompts_file = os.path.join(self.base_dir, "config", "gemini_prompts.json")
        self.char_prompts_file = os.path.join(self.base_dir, "config", "gemini_character_prompts.json")
        
        # 모듈 초기화
        self.camera = CameraCapture()
        self.cropper = HumanCropper()
        self.gui = GUIViewer()
        
        # 설정 및 상태
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.prompts_dict = self.load_prompts()
        self.char_prompts_dict = self.load_character_prompts()
        self.gemini_prompt = ""
        self.character_image = None # 캐릭터 동반 모드용 이미지
        
        # 실행 폴더 자동 생성
        os.makedirs(self.data_dir, exist_ok=True)

    def load_prompts(self):
        """JSON 파일에서 Gemini 프롬프트 목록을 로드합니다."""
        default_prompts = {
            "1. 고품질 라인 아트 (권장)": "A high-quality, pure black line art caricature. Draw only the main person. The entire drawing must be rendered exclusively with lines of exactly the same thickness (uniform line weight, minimal width) using only solid black ink. No solid fills, shading, or gradients. Hollow eyes. Machine-drawn style for direct plotting.",
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
            print(f"[오류] 프롬프트 파일을 읽는 중 오류 발생: {e}")
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

        # 캐릭터 동반 모드인 경우 캐릭터 이미지 로드 확인
        if is_character_mode:
            print(f"\n[{mode_name}] 모드를 시작합니다. 함께 그릴 캐릭터 이미지를 선택하세요.")
            char_path = input("캐릭터 이미지 경로 (기본값: modules/models/character.png): ").strip()
            if not char_path:
                char_path = os.path.join(self.base_dir, "modules", "models", "character.png")
            
            if os.path.exists(char_path):
                self.character_image = cv2.imread(char_path)
                if self.character_image is not None:
                    print(f">> 캐릭터 이미지가 로드되었습니다: {os.path.basename(char_path)}")
                else:
                    print("[오류] 이미지 파일을 읽을 수 없습니다.")
                    return False
            else:
                print(f"[오류] 파일이 존재하지 않습니다: {char_path}")
                # 테스트용 더미 생성 혹은 중단
                return False

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
                print(f">> [배치 모드] 모든 {len(prompt_keys)}개 스타일을 순차적으로 하나씩 실행합니다.")
            elif not p_input:
                self.gemini_prompt = current_prompts[prompt_keys[0]]
                print(f">> '1. {prompt_keys[0]}' 스타일(기본값)이 적용되었습니다.")
            else:
                p_choice = int(p_input)
                if 1 <= p_choice <= len(prompt_keys):
                    selected_key = prompt_keys[p_choice - 1]
                    self.gemini_prompt = current_prompts[selected_key]
                    print(f">> '{p_choice}. {selected_key}' 스타일이 적용되었습니다.")
                elif p_choice == len(prompt_keys) + 1:
                    self.gemini_prompt = input("프롬프트를 직접 입력하세요: ").strip()
                else:
                    self.gemini_prompt = current_prompts[prompt_keys[0]]
        except (ValueError, IndexError):
            self.gemini_prompt = current_prompts[prompt_keys[0]]
        
        return True if self.gemini_prompt else False

    def run(self):
        """메인 실행 루프"""
        while True:
            print("\n" + "="*50)
            print(" [이미지 기반 로봇 선화 추출 시스템]")
            print("="*50)
            print(" 1. 사진 촬영 및 스케치 (AI - Anime 스타일)")
            print(" 2. 사진 촬영 및 스케치 (Gemini - 선화 스타일)")
            print(" 3. 사진 촬영 및 스케치 (Gemini - 캐릭터 동반 모드)")
            print(" 4. 이미지 세선화 (기존 이미지 파일 사용)")
            print(" q. 종료")
            print("="*50)
            
            choice = input("선택하세요: ").strip().lower()
            
            if choice == '1':
                self.process_with_capture('AI_ANIME')
            elif choice == '2':
                if self.check_gemini_config(is_character_mode=False):
                    self.process_with_capture('GEMINI')
            elif choice == '3':
                if self.check_gemini_config(is_character_mode=True):
                    self.process_with_capture('GEMINI_CHAR')
            elif choice == '4':
                self.process_local_file()
            elif choice == 'q':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

    def process_with_capture(self, sketch_type):
        """사진을 촬영하고 선택한 모드로 스케치를 생성합니다."""
        # 1. 사진 촬영
        print("\n>> 카메라를 활성화합니다. (Space: 촬영, Q: 취소)")
        raw_image = self.camera.capture()
        if raw_image is None:
            return

        # 2. 전처리 (크롭 및 세션 디렉토리 생성)
        processed_img, intermediate_dir, output_dir = self.preprocess_image(raw_image)
        if processed_img is None:
            return

        base_filename = datetime.datetime.now().strftime("%H%M%S")
        
        # 3. 스케치 생성 및 세선화
        self.process_and_save(processed_img, sketch_type, base_filename, intermediate_dir, output_dir)

    def process_local_file(self):
        """로컬 이미지 파일을 불러와 세선화를 진행합니다."""
        path = input("이미지 파일 경로: ").strip()
        if not os.path.exists(path):
            print("[오류] 파일이 없습니다.")
            return
            
        img = cv2.imread(path)
        if img is None:
            print("[오류] 이미지를 읽을 수 없습니다.")
            return

        # 세션 디렉토리 생성
        processed_img, intermediate_dir, output_dir = self.preprocess_image(img)
        base_filename = os.path.splitext(os.path.basename(path))[0]
        
        # 세선화 진행 (여기서는 간단히 Canny/Binary 선택 가능하게 할 수도 있음)
        nc_path = os.path.join(output_dir, f"{base_filename}_local.nc")
        svg_path = os.path.join(output_dir, f"{base_filename}_local.svg")
        
        gray = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        
        generate_files_thinning(binary, nc_path, svg_path)
        print(f">> 완료: {nc_path}")

    def preprocess_image(self, image):
        """이미지를 세션별 폴더에 저장하고 전처리를 수행합니다."""
        session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        session_dir = os.path.join(self.data_dir, f"{session_id}_session")
        intermediate_dir = os.path.join(session_dir, "intermediate")
        output_dir = os.path.join(session_dir, "output")
        
        os.makedirs(intermediate_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # 원본 저장
        cv2.imencode(".jpg", image)[1].tofile(os.path.join(intermediate_dir, "01_raw.jpg"))
        
        # 인물 크롭
        cropped = self.cropper.crop(image)
        if cropped is None:
            print("[경고] 인물을 감지하지 못했습니다. 원본을 사용합니다.")
            cropped = image
        
        cv2.imencode(".jpg", cropped)[1].tofile(os.path.join(intermediate_dir, "02_cropped.jpg"))

        # 이미지 보정
        preprocessed = image_processor(cropped)
        if preprocessed is None:
            preprocessed = cropped

        cv2.imencode(".jpg", preprocessed)[1].tofile(os.path.join(intermediate_dir, "03_preprocessed.jpg"))
        return preprocessed, intermediate_dir, output_dir

    def process_and_save(self, image, sketch_type, base_filename, intermediate_dir, output_dir):
        """AI 스케치 생성 후 세선화를 거쳐 G-코드로 저장합니다. (Batch 모드 지원)"""
        
        # Gemini 배치 모드 처리 (딕셔너리인 경우)
        if (sketch_type == 'GEMINI' or sketch_type == 'GEMINI_CHAR') and isinstance(self.gemini_prompt, dict):
            print(f"\n>> [일괄 순차 처리 시작] 총 {len(self.gemini_prompt)}개의 스타일을 하나씩 적용합니다.")
            
            for i, (style_name, prompt_text) in enumerate(self.gemini_prompt.items(), 1):
                safe_style_name = "".join([c if c.isalnum() else "_" for c in style_name])
                current_base = f"{base_filename}_{safe_style_name}"
                
                print(f"\n[{style_name}] ({i}/{len(self.gemini_prompt)}) 작업 시작...")
                self._single_process_and_save(image, sketch_type, prompt_text, current_base, intermediate_dir, output_dir, style_name)
        else:
            # 단일 모드 처리
            self._single_process_and_save(image, sketch_type, self.gemini_prompt, base_filename, intermediate_dir, output_dir, "단일 모드")

    def _single_process_and_save(self, image, sketch_type, prompt, base_filename, intermediate_dir, output_dir, style_name="Default"):
        """실제 한 장의 이미지를 변환하고 저장하는 내부 메서드"""
        # GUI 초기화
        self.gui.clear_panels()
        self.gui.update_image(0, image) # 1단계: 원본 표시

        if sketch_type == 'AI_ANIME':
            sketch = generate_sketch(image)
            threshold_val = 220
            suffix = "anime"
        else: # GEMINI or GEMINI_CHAR
            sketch = generate_gemini_sketch(
                image, 
                api_key=self.gemini_api_key, 
                prompt=prompt,
                style_name=style_name,
                character_image_bgr=self.character_image
            )
            threshold_val = 240
            suffix = "gemini"

        if sketch is None:
            print(f"[{style_name}] [오류] '{base_filename}' 스케치 생성 실패")
            return
        
        # 2단계: AI 스케치 GUI 표시
        self.gui.update_image(1, sketch)

        output_base = f"{base_filename}_{suffix}"
        cv2.imencode(".png", sketch)[1].tofile(os.path.join(intermediate_dir, f"{output_base}.png"))

        if len(sketch.shape) == 3:
            sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(sketch, threshold_val, 255, cv2.THRESH_BINARY)
        
        # 3단계: 세선화 결과(이진화 이미지) GUI 표시
        self.gui.update_image(2, binary)
        
        print(f"[{style_name}] >> [세선화 및 G-코드 생성] {output_base}")
        nc_path = os.path.join(output_dir, f"{output_base}.nc")
        svg_path = os.path.join(output_dir, f"{output_base}.svg")
        generate_files_thinning(binary, nc_path, svg_path)
        print(f"[{style_name}] >> 완료: {output_base}.nc")

if __name__ == "__main__":
    app = SketchApp()
    app.run()
