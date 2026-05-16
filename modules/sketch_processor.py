import os
import cv2
import numpy as np
import shutil
from modules import (
    config,
    image_processor,
    generate_files_thinning,
    detect_person_and_get_roi,
    detect_face_and_get_roi,
    generate_sketch,
    generate_gemini_sketch
)

class SketchProcessor:
    def __init__(self):
        # 세션 초기화는 최초 1회만 수행 (이미 되어있을 수도 있음)
        config.initialize_session()
        self.photo_counter = 1

    def process(self, image, sketch_type, gemini_api_key=None, gemini_prompt=None, 
                character_image=None, pen_config=None, progress_callback=None, temperature=0.0):
        """
        이미지를 처리하여 스케치 및 G-Code를 생성합니다.
        
        Args:
            image: 원본 이미지 (numpy array, BGR)
            sketch_type: 'AI_ANIME', 'GEMINI', 'GEMINI_CHAR'
            gemini_api_key: Gemini API 키
            gemini_prompt: Gemini 프롬프트 문자열 (또는 배치 모드일 경우 딕셔너리)
            character_image: 합성할 캐릭터 이미지 (BGR)
            pen_config: PenConfig 객체 (Z_SAFE, Z_DRAW 등 포함)
            progress_callback: 단계별 이미지 및 메시지 전달을 위한 콜백 함수 
                               signature: callback(step_id, image, message)
            temperature: Gemini AI의 온값 (0.0: 일관성, 1.0: 창의성)
        """
        if pen_config is None:
            pen_config = config.PEN_PRESETS["네임펜"]

        # 사진별 저장 경로 설정
        photo_name = f"{self.photo_counter}_gui_capture"
        input_dir, intermediate_dir, output_dir = config.setup_photo_paths(photo_name)
        
        # 1. 원본 저장 및 콜백
        if progress_callback:
            progress_callback("original", image, "원본 이미지를 로드했습니다.")
        cv2.imencode(".jpg", image)[1].tofile(os.path.join(input_dir, "original.jpg"))

        # 2. 전처리 (얼굴 우선, 없으면 사람/상체 추출)
        # 카메라 화면에서 보여주는 ROI와 일치시키기 위해 detect_face_and_get_roi를 우선 시도
        roi = detect_face_and_get_roi(image)
        roi_type = "얼굴"
        
        if roi is None:
            roi = detect_person_and_get_roi(image)
            roi_type = "사람/상체"

        if roi:
            x1, y1, x2, y2 = roi
            # 정확한 슬라이싱: [y1:y2, x1:x2]
            cropped = image[y1:y2, x1:x2]
            if progress_callback:
                progress_callback("cropped", cropped, f"{roi_type} 영역을 A4 비율로 추출했습니다.")
        else:
            cropped = image
            if progress_callback:
                progress_callback("cropped", cropped, "객체를 감지하지 못해 원본 전체를 사용합니다.")

        preprocessed = image_processor(cropped)
        if preprocessed is None:
            preprocessed = cropped
        
        if progress_callback:
            progress_callback("preprocessed", preprocessed, "이미지 보정 및 배경 처리를 완료했습니다.")
        cv2.imencode(".jpg", preprocessed)[1].tofile(os.path.join(intermediate_dir, "preprocessed.jpg"))

        # 3. 스케치 생성
        results = []
        if (sketch_type == 'GEMINI' or sketch_type == 'GEMINI_CHAR') and isinstance(gemini_prompt, dict):
            # 일괄 처리 모드
            for i, (style_name, prompt_text) in enumerate(gemini_prompt.items(), 1):
                safe_style_name = "".join([c if c.isalnum() else "_" for c in style_name])
                res = self._single_generate(preprocessed, sketch_type, prompt_text, character_image, 
                                          f"photo_{safe_style_name}", intermediate_dir, output_dir, 
                                          pen_config, progress_callback, gemini_api_key, temperature)
                results.append(res)
        else:
            # 단일 처리 모드
            res = self._single_generate(preprocessed, sketch_type, gemini_prompt, character_image, 
                                      "photo", intermediate_dir, output_dir, 
                                      pen_config, progress_callback, gemini_api_key, temperature)
            results.append(res)

        self.photo_counter += 1
        return results

    def _single_generate(self, image, sketch_type, prompt, character_image, base_filename, 
                         intermediate_dir, output_dir, pen_config, progress_callback, api_key, temperature):
        
        # GEMINI or GEMINI_CHAR
        if progress_callback:
            progress_callback("gemini_start", None, "Gemini AI가 스케치를 생성 중입니다...")
        
        # API 키가 명시적으로 전달되지 않았으면 환경변수 사용
        final_api_key = api_key if api_key else os.getenv("GEMINI_API_KEY")
        
        # generate_gemini_sketch 내부에서 예외를 발생시키므로 여기서도 예외가 발생함
        sketch = generate_gemini_sketch(
            image, 
            api_key=final_api_key, 
            prompt=prompt,
            character_image_bgr=character_image,
            temperature=temperature
        )
        threshold_val = 240
        suffix = "gemini"

        if sketch is None:
            raise RuntimeError(f"'{base_filename}' 스케치 생성 실패: 결과가 없습니다.")

        if progress_callback:
            progress_callback("sketch", sketch, "스케치 생성이 완료되었습니다.")

        output_base = f"{base_filename}_{suffix}"
        cv2.imencode(".png", sketch)[1].tofile(os.path.join(intermediate_dir, f"{output_base}.png"))

        # 4. G-Code 생성
        if sketch.ndim == 3:
            channels = sketch.shape[2]
            if channels == 1:
                sketch = sketch[:, :, 0]
            elif channels == 3:
                sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
            elif channels == 4:
                sketch = cv2.cvtColor(sketch, cv2.COLOR_BGRA2GRAY)
            else:
                raise ValueError(f"Unsupported sketch channel count: {channels}")
        _, binary = cv2.threshold(sketch, threshold_val, 255, cv2.THRESH_BINARY)
        
        nc_path = os.path.join(output_dir, f"{output_base}.nc")
        svg_path = os.path.join(output_dir, f"{output_base}.svg")
        
        # PenConfig 적용 (임시로 전역 변수 덮어쓰기 - generate_files_thinning 내부 구조에 따라 다름)
        # 만약 generate_files_thinning이 config.Z_SAFE 등을 직접 참조한다면 덮어써야 함.
        import modules.config as cfg
        old_z_safe, old_z_draw, old_feed, old_scale = cfg.Z_SAFE, cfg.Z_DRAW, cfg.FEED_RATE, cfg.SCALE
        
        cfg.Z_SAFE = pen_config.z_safe
        cfg.Z_DRAW = pen_config.z_draw
        cfg.FEED_RATE = pen_config.feed_rate
        cfg.SCALE = pen_config.scale
        
        try:
            generate_files_thinning(binary, nc_path, svg_path)
        finally:
            # 원상 복구
            cfg.Z_SAFE, cfg.Z_DRAW, cfg.FEED_RATE, cfg.SCALE = old_z_safe, old_z_draw, old_feed, old_scale

        if progress_callback:
            progress_callback("done", binary, f"G-Code 생성 완료: {output_base}.nc")

        return nc_path
