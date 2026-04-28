try:
    import pyzed.sl as sl
    ZED_AVAILABLE = True
except ImportError:
    ZED_AVAILABLE = False
import cv2
import time
import os
import numpy as np
from .human_cropper import detect_person_and_get_roi, detect_face_and_get_roi

def draw_guide_frames(frame):
    """프레임 위에 상체와 얼굴 가이드 라인을 그립니다."""
    # 1. 상체 감지 시도
    person_roi = detect_person_and_get_roi(frame)
    if person_roi:
        x, y, w, h = person_roi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2) # 하늘색: 상체
        
        # 2. 상체 영역 내에서 얼굴 감지 시도
        person_img = frame[y:y+h, x:x+w]
        face_roi = detect_face_and_get_roi(person_img)
        if face_roi:
            fx1, fy1, fx2, fy2 = face_roi
            # 전체 프레임 좌표로 변환하여 그리기
            cv2.rectangle(frame, (x + fx1, y + fy1), (x + fx2, y + fy2), (0, 255, 255), 2) # 노란색: 얼굴
    
    return frame

def run_zed_capture(save_dir=None):
    """
    ZED 카메라를 사용하여 이미지를 1회 캡처하고 지정된 경로에 저장합니다.
    가이드 라인 표시 기능이 포함되어 있습니다.
    
    - SPACE: 사진 촬영 (단일 프레임 캡처)
    - ESC  : 취소
    
    Args:
        save_dir (str, optional): 이미지를 저장할 디렉토리. None이면 기본 경로 사용.
    반환값:
        촬영 성공 시 -> 저장된 이미지 경로 (str)
        종료/실패 시 -> None
    """
    if not ZED_AVAILABLE:
        print("\n[오류] ZED SDK가 설치되어 있지 않거나 pyzed 모듈을 찾을 수 없습니다.")
        print("일반 웹캠 모드(Photo Booth)를 사용해 주세요.")
        return None
    
    # 저장 경로 설정
    if not save_dir:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        save_dir = os.path.join(BASE_DIR, "data", "raw")
    
    os.makedirs(save_dir, exist_ok=True)

    # ZED 객체 생성 및 초기화
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.depth_mode = sl.DEPTH_MODE.NONE

    # 카메라 오픈
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"❌ ZED 카메라 열기 실패: {err}")
        return None

    # 이미지 저장 객체
    image_zed = sl.Mat()
    captured_path = None

    print("\n>> ZED 카메라 프리뷰 (SPACE: 촬영, ESC: 취소)")
    
    try:
        while True:
            # 한 프레임 grab
            if zed.grab() == sl.ERROR_CODE.SUCCESS:
                # 왼쪽 카메라 이미지 가져오기
                zed.retrieve_image(image_zed, sl.VIEW.LEFT)
                
                # OpenCV 형식 변환 (ZED 이미지는 BGRA 형태)
                img_bgra = image_zed.get_data()
                # 프리뷰 및 저장을 위해 BGR로 변환
                img_bgr = cv2.cvtColor(img_bgra, cv2.COLOR_BGRA2BGR)
                
                # 가이드 라인 표시용 복사본 생성 (원본은 그대로 보존)
                display_frame = img_bgr.copy()
                display_frame = draw_guide_frames(display_frame)
                
                # UI 요소 추가 (버튼 안내)
                h, w, _ = display_frame.shape
                cv2.rectangle(display_frame, (w // 2 - 120, h - 80), (w // 2 + 120, h - 30), (0, 255, 0), -1)
                cv2.putText(display_frame, "TAKE PHOTO (SPACE)", (w // 2 - 100, h - 45), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
                
                # 화면에 표시
                cv2.imshow("ZED Camera Preview", display_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == 32: # SPACE
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    filename = f"zed_capture_{timestamp}.png"
                    captured_path = os.path.join(save_dir, filename)
                    
                    # 저장 (원본 이미지 img_bgr 사용)
                    result, encoded_img = cv2.imencode(".png", img_bgr)
                    if result:
                        with open(captured_path, "wb") as f:
                            encoded_img.tofile(f)
                        print(f"📸 ZED 사진 저장 완료: {captured_path}")
                    else:
                        print("❌ 이미지 인코딩 실패")
                        captured_path = None
                    break
                    
                elif key == 27: # ESC
                    print(">> ZED 촬영이 취소되었습니다.")
                    break
            else:
                print("❌ ZED 프레임 그랩 실패")
                break
    finally:
        zed.close()
        cv2.destroyWindow("ZED Camera Preview")

    return captured_path

if __name__ == "__main__":
    # 테스트 코드
    path = run_zed_capture()
    if path:
        print(f"Captured: {path}")
