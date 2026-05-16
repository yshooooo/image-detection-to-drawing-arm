import os
import cv2
import numpy as np
import time
from google import genai
from google.genai import types

# --- Gemini API 설정 ---
MODEL_ID = "gemini-3.1-flash-image-preview"

def generate_gemini_sketch(image_bgr: np.ndarray, api_key: str = None, prompt: str = None, style_name: str = "Gemini", character_image_bgr: np.ndarray = None, temperature: float = 0.0) -> np.ndarray:
    """
    OpenCV 이미지를 입력받아 Gemini API를 사용하여 세선화에 최적화된 고품질 선화를 생성합니다.
    """
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print(f"\n[{style_name}] [오류] GEMINI_API_KEY가 설정되지 않았습니다.")
        return None

    # --- 1. 입력 이미지 전처리 (정규화) ---
    # CLAHE(Contrast Limited Adaptive Histogram Equalization)를 적용하여 조명 편차를 줄입니다.
    lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    processed_image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # --- 2. 시스템 인스트럭션 및 프롬프트 설정 ---
    system_instruction = (
        "You are an expert line art illustrator specializing in minimalist vector art for pen plotters. "
        "Your absolute priority is to create drawings composed ONLY of solid black lines on a pure white background. "
        "RULES: "
        "1. NO shading, NO gradients, NO colors, NO gray areas. "
        "2. All lines must have a CONSISTENT thickness (monoline). "
        "3. Focus on essential contours and clear shapes. "
        "4. Avoid fine details like skin wrinkles, small shadows, or complex textures. "
        "5. Lines must be clean and continuous for robotic tracing."
    )

    if not prompt:
        if character_image_bgr is not None:
            prompt = (
                "Combine the person and the character into a single cohesive line art scene. "
                "Draw them interacting naturally. "
                "Ensure NO facial wrinkles or aging lines are drawn on the person. "
                "The eyes must be clean outlines. NO solid black fills unless it's a very small dot for the pupil. "
                "The result must be a high-quality, pure black monoline drawing on a white background."
            )
        else:
            prompt = (
                "A minimalist, high-quality black line art caricature based on the provided image. "
                "Render the person with smooth, clean lines. "
                "ABSOLUTELY NO shading, hatching, or textures. "
                "DO NOT draw any wrinkles, smile lines, or fine facial details. "
                "The eyes should be represented as clear, open outlines. "
                "The hair should be simplified into a few smooth, sweeping paths. "
                "The result must be optimized for a robotic arm drawing with a single pen."
            )

    print(f">> [{style_name}] Gemini API({MODEL_ID})를 사용하여 선화 추출을 시작합니다.")

    # 재시도 설정
    max_retries = 3
    retry_delay = 5  # 초

    for attempt in range(1, max_retries + 1):
        start_time = time.time()
        try:
            # OpenCV 이미지(BGR)를 PNG 바이트로 인코딩
            success, encoded_image = cv2.imencode(".png", processed_image)
            if not success:
                print(f"[{style_name}] [오류] 메인 이미지 인코딩에 실패했습니다.")
                return None
            
            parts = [
                types.Part(text=prompt),
                types.Part(
                    inline_data=types.Blob(
                        data=encoded_image.tobytes(),
                        mime_type="image/png"
                    )
                )
            ]

            if character_image_bgr is not None:
                success_char, encoded_char = cv2.imencode(".png", character_image_bgr)
                if success_char:
                    parts.append(types.Part(inline_data=types.Blob(data=encoded_char.tobytes(), mime_type="image/png")))

            # Gemini 클라이언트 설정
            client = genai.Client(api_key=api_key)

            # Gemini API 호출 (System Instruction 및 Seed 추가)
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[types.Content(role="user", parts=parts)],
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_modalities=["IMAGE"],
                    temperature=temperature,
                    top_k=1,
                    seed=42, # 일관성을 위한 시드 고정
                )
            )

            # 4. 결과 처리 (첫 번째 이미지 추출)
            result_sketch = None
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    nparr = np.frombuffer(part.inline_data.data, np.uint8)
                    result_sketch = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    break
                elif part.text:
                    print(f"   [{style_name}] [Gemini 메시지] {part.text}")

            elapsed_time = time.time() - start_time
            if result_sketch is None:
                print(f"   [{style_name}] [오류] 이미지가 생성되지 않았습니다. (소요 시간: {elapsed_time:.2f}초)")
                return None

            # 5. 후처리 (원본 크기로 맞추기 및 그레이스케일 변환)
            h, w = image_bgr.shape[:2]
            # INTER_CUBIC은 LANCZOS4보다 부드러운 결과를 보여 계단 현상을 완화합니다.
            final_sketch = cv2.resize(result_sketch, (w, h), interpolation=cv2.INTER_CUBIC)
            
            if len(final_sketch.shape) == 3:
                final_sketch = cv2.cvtColor(final_sketch, cv2.COLOR_BGR2GRAY)

            print(f"   [{style_name}] >> 생성 성공! (소요 시간: {elapsed_time:.2f}초)")
            return final_sketch

        except Exception as e:
            elapsed_time = time.time() - start_time
            print(f"   [{style_name}] [시도 {attempt}/{max_retries} 실패] 오류: {e} (소요 시간: {elapsed_time:.2f}초)")
            
            if attempt < max_retries:
                print(f"   [{style_name}] {retry_delay}초 후 다시 시도합니다...")
                time.sleep(retry_delay)
            else:
                print(f"   [{style_name}] [최종 실패] 모든 재시도 횟수를 초과했습니다.")
                return None
    return None
