import os
import cv2
import numpy as np
import time
from google import genai
from google.genai import types

# --- Gemini API 설정 ---
MODEL_ID = "gemini-3.1-flash-image-preview"

def generate_gemini_sketch(image_bgr: np.ndarray, api_key: str = None, prompt: str = None, style_name: str = "Gemini", character_image_bgr: np.ndarray = None) -> np.ndarray:
    """
    OpenCV 이미지를 입력받아 Gemini API를 사용하여 세선화에 최적화된 고품질 선화를 생성합니다.
    서버 과부하(503 등) 발생 시 자동으로 재시도하며 실행 시간을 측정합니다.
    character_image_bgr이 제공되면 두 이미지를 합성하여 그립니다.
    """
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print(f"\n[{style_name}] [오류] GEMINI_API_KEY가 설정되지 않았습니다.")
        return None

    if not prompt:
        if character_image_bgr is not None:
            prompt = (
                "Combine the person from the first image and the character from the second image into a single, cohesive scene. "
                "Draw them interacting or standing together naturally. "
                "Render the entire drawing as a high-quality, pure black line art caricature. "
                "The entire drawing must be rendered exclusively with lines of exactly the same thickness (uniform line weight, minimal width) using only solid black ink. "
                "Only solid black lines on a clean white background. No filling, shading, or gradients. "
                "The lines should be precise and appear machine-drawn for direct path tracing."
            )
        else:
            prompt = (
                "A high-quality, pure black line art caricature based on the provided image. "
                "The entire drawing is rendered exclusively with lines of exactly the same thickness "
                "(uniform line weight, minimal width) using only solid black ink. "
                "The lines are precise, unwavering, and appear machine-drawn for direct path tracing. "
                "Only solid black lines on a clean white background. "
                "No other colors, gradients, shading, or textures are present. "
                "Minimalist geometric details. Focus purely on the continuity of the lines and the main simplified shape."
            )

    print(f">> [{style_name}] Gemini API({MODEL_ID})를 사용하여 선화 추출을 시작합니다.")

    # 재시도 설정
    max_retries = 3
    retry_delay = 5  # 초

    for attempt in range(1, max_retries + 1):
        start_time = time.time()
        try:
            # 1. OpenCV 이미지(BGR)를 PNG 바이트로 인코딩
            success, encoded_image = cv2.imencode(".png", image_bgr)
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

            # 캐릭터 이미지가 있으면 추가
            if character_image_bgr is not None:
                success_char, encoded_char = cv2.imencode(".png", character_image_bgr)
                if success_char:
                    parts.append(
                        types.Part(
                            inline_data=types.Blob(
                                data=encoded_char.tobytes(),
                                mime_type="image/png"
                            )
                        )
                    )
                else:
                    print(f"[{style_name}] [경고] 캐릭터 이미지 인코딩 실패, 메인 이미지만 사용합니다.")

            # 2. Gemini 클라이언트 설정
            client = genai.Client(api_key=api_key)

            # 3. Gemini API 호출
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[types.Content(role="user", parts=parts)],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"]
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
