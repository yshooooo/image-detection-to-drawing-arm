import cv2
import numpy as np
import urllib.request
import os
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

# ─── 모델 파일 자동 다운로드 ──────────────────────────────────────────────────
# MediaPipe 0.10+ 은 .tflite / .task 모델 파일을 직접 로드합니다.
# 파일이 없으면 Google 공식 저장소에서 자동으로 다운받습니다.

_MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
os.makedirs(_MODEL_DIR, exist_ok=True)

_FACE_MODEL_PATH = os.path.join(_MODEL_DIR, "face_detection_short_range.tflite")
_POSE_MODEL_PATH = os.path.join(_MODEL_DIR, "pose_landmarker_lite.task")

_FACE_MODEL_URL = "https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/latest/blaze_face_short_range.tflite"
_POSE_MODEL_URL = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task"

def _download_if_missing(path: str, url: str) -> None:
    """모델 파일이 없으면 다운로드합니다."""
    if not os.path.exists(path):
        filename = os.path.basename(path)
        print(f"[모델 다운로드] {filename} 다운로드 중...")
        urllib.request.urlretrieve(url, path)
        print(f"[모델 다운로드] {filename} 완료 → {path}")

_download_if_missing(_FACE_MODEL_PATH, _FACE_MODEL_URL)
_download_if_missing(_POSE_MODEL_PATH, _POSE_MODEL_URL)


# ─── MediaPipe Tasks API 초기화 ───────────────────────────────────────────────
#
# [구버전 0.9 vs 신버전 0.10+ 차이점]
#
# 구버전:  mp.solutions.face_detection.FaceDetection(...)
#           → mp.Image 불필요, numpy 배열 직접 전달
#
# 신버전:  vision.FaceDetector.create_from_options(options)
#           → 반드시 mp.Image 로 변환 후 전달
#           → 모델 파일(.tflite / .task) 필요
#           → 결과 좌표가 "절대 픽셀값" 으로 반환 (구버전은 0~1 상대값)
#

# ─── 모델 파일을 Python이 직접 읽어 bytes로 전달 ─────────────────────────────
# main.py의 np.fromfile 방식과 동일한 원리:
# C++ 레이어가 한글 경로를 직접 열면 실패하므로,
# Python(유니코드 지원)이 먼저 읽고 bytes로 넘겨서 경로 문제를 우회합니다.
with open(_FACE_MODEL_PATH, 'rb') as f:
    _face_model_buffer = f.read()

with open(_POSE_MODEL_PATH, 'rb') as f:
    _pose_model_buffer = f.read()

# 얼굴 감지기 (단거리 모델: 웹캠 거리에 최적)
_face_options = vision.FaceDetectorOptions(
    base_options=mp_python.BaseOptions(model_asset_buffer=_face_model_buffer),
    min_detection_confidence=0.5
)
face_detector = vision.FaceDetector.create_from_options(_face_options)

# 포즈(상체) 감지기
_pose_options = vision.PoseLandmarkerOptions(
    base_options=mp_python.BaseOptions(model_asset_buffer=_pose_model_buffer),
    running_mode=vision.RunningMode.VIDEO,
    min_pose_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    num_poses=1
)
pose_detector = vision.PoseLandmarker.create_from_options(_pose_options)

# VIDEO 모드는 타임스탬프가 필요 → 프레임마다 증가시킬 카운터
_frame_timestamp_ms = 0


# ─── 상수 ────────────────────────────────────────────────────────────────────
A4_RATIO = 210 / 297  # ≈ 0.707 (width / height)
A5_RATIO = A4_RATIO   # A5와 A4는 가로세로 비율이 동일함

# 상체 ROI 계산에 사용할 랜드마크 인덱스
# PoseLandmarker 랜드마크 목록: https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
_UPPER_BODY_IDX = [0, 11, 12, 13, 14]
# 0=코, 11=왼어깨, 12=오른어깨, 13=왼팔꿈치, 14=오른팔꿈치 (골반 제외 → 중심 쏠림 방지)


# ─── 내부 유틸 ────────────────────────────────────────────────────────────────

def _to_mp_image(image: np.ndarray) -> mp.Image:
    """
    OpenCV BGR numpy 배열을 MediaPipe Image 로 변환합니다.
    신버전 Tasks API 는 mp.Image 만 입력으로 받습니다.
    """
    if image.ndim == 2:
        rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    else:
        channels = image.shape[2]
        if channels == 1:
            rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif channels == 3:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif channels == 4:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        else:
            raise ValueError(f"Unsupported image channel count: {channels}")
    return mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)


def _adjust_roi_to_ratio(
    x1: int, y1: int, x2: int, y2: int,
    frame_h: int, frame_w: int,
    ratio: float = A4_RATIO
) -> tuple:
    """
    ROI를 지정 비율(width/height)로 중심 유지하며 조정합니다.
    프레임 경계를 벗어나지 않도록 클리핑합니다.
    """
    roi_w = x2 - x1
    roi_h = y2 - y1
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    current_ratio = roi_w / roi_h if roi_h > 0 else ratio

    if current_ratio > ratio:
        # 가로가 비율보다 길면 세로를 늘림
        new_w = roi_w
        new_h = int(roi_w / ratio)
    else:
        # 세로가 비율보다 길면 가로를 늘림
        new_h = roi_h
        new_w = int(roi_h * ratio)

    # 중심 유지하며 새로운 좌표 계산
    nx1 = cx - new_w // 2
    ny1 = cy - new_h // 2
    nx2 = nx1 + new_w
    ny2 = ny1 + new_h

    # 프레임 범위를 벗어날 경우 이동(Shift)하여 최대한 영역 확보
    if nx1 < 0:
        nx2 -= nx1
        nx1 = 0
    if ny1 < 0:
        ny2 -= ny1
        ny1 = 0
    if nx2 > frame_w:
        nx1 -= (nx2 - frame_w)
        nx2 = frame_w
    if ny2 > frame_h:
        ny1 -= (ny2 - frame_h)
        ny2 = frame_h

    # 최종 클리핑 (여전히 벗어나는 경우 대비)
    nx1, ny1 = max(0, nx1), max(0, ny1)
    nx2, ny2 = min(frame_w, nx2), min(frame_h, ny2)

    return int(nx1), int(ny1), int(nx2), int(ny2)


# ─── 공개 함수 ────────────────────────────────────────────────────────────────

def detect_person_and_get_roi(image: np.ndarray) -> tuple | None:
    """
    MediaPipe PoseLandmarker로 상체 ROI를 반환합니다.
    A4 비율이 적용된 (x1, y1, x2, y2)를 반환합니다.
    """
    global _frame_timestamp_ms
    _frame_timestamp_ms += 33  # 약 30fps 기준 타임스탬프 증가

    h, w = image.shape[:2]
    result = pose_detector.detect_for_video(_to_mp_image(image), _frame_timestamp_ms)

    # 감지된 사람이 없으면 None
    if not result.pose_landmarks:
        return None

    # 첫 번째 사람(num_poses=1 이므로 항상 인덱스 0)
    landmarks = result.pose_landmarks[0]

    xs, ys = [], []
    for idx in _UPPER_BODY_IDX:
        lm = landmarks[idx]
        if lm.visibility > 0.3:
            xs.append(int(lm.x * w))
            ys.append(int(lm.y * h))

    if len(xs) < 2:
        return None

    # 기본 바운딩 박스
    x1, y1 = min(xs), min(ys)
    x2, y2 = max(xs), max(ys)

    # 여유 공간 추가
    pad_w = int((x2 - x1) * 0.2)
    pad_top = int((y2 - y1) * 0.6)
    pad_bottom = int((y2 - y1) * 0.2)

    nx1 = max(0, x1 - pad_w)
    ny1 = max(0, y1 - pad_top)
    nx2 = min(w, x2 + pad_w)
    ny2 = min(h, y2 + pad_bottom)

    # A4 비율 조정
    return _adjust_roi_to_ratio(nx1, ny1, nx2, ny2, h, w)


def detect_face_and_get_roi(image: np.ndarray) -> tuple | None:
    """
    MediaPipe FaceDetector로 얼굴을 감지하고 A4 비율 ROI를 반환합니다.
    """
    h, w = image.shape[:2]
    result = face_detector.detect(_to_mp_image(image))

    if not result.detections:
        return None

    # confidence 가장 높은 얼굴 선택
    best = max(result.detections, key=lambda d: d.categories[0].score)
    bb = best.bounding_box

    fx, fy   = bb.origin_x, bb.origin_y
    fw, fh   = bb.width,    bb.height

    # 얼굴 여백 추가
    pad_w        = int(fw * 0.4)
    pad_top      = int(fh * 0.8)
    pad_bottom   = int(fh * 0.4)
    x1 = max(0, fx - pad_w)
    y1 = max(0, fy - pad_top)
    x2 = min(w, fx + fw + pad_w)
    y2 = min(h, fy + fh + pad_bottom)

    # A4 비율 조정
    return _adjust_roi_to_ratio(x1, y1, x2, y2, h, w)
