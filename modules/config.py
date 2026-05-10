import os
import datetime
import json

# --- 기본 경로 설정 ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
# 사용자가 이미지를 넣는 공용 폴더
GENERAL_INPUT_DIR = os.path.join(DATA_DIR, "raw") 
# 사용자가 직접 넣어둘 로컬 G-code 파일 경로
LOCAL_GCODE_PATH = os.path.join(DATA_DIR, "local_robot_input.nc")
# 합성용 캐릭터 이미지가 저장되는 폴더
CHARACTERS_DIR = os.path.join(DATA_DIR, "characters")

# 프롬프트 설정 파일 경로
PROMPTS_FILE = os.path.join(BASE_DIR, "config", "gemini_prompts.json")
CHAR_PROMPTS_FILE = os.path.join(BASE_DIR, "config", "gemini_character_prompts.json")

def _load_json_prompts(file_path, default_data):
    if not os.path.exists(file_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=4, ensure_ascii=False)
        except Exception:
            pass
        return default_data
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if data else default_data
    except Exception:
        return default_data

def load_prompts():
    default_prompts = {
        "1. 세선화 최적화 (기본)": "A high-quality, pure black line art caricature based on the provided image. The entire drawing is rendered exclusively with lines of exactly the same thickness (uniform line weight, minimal width) using only solid black ink. DO NOT FILL ANY AREAS with solid color. Draw everything, including eyes and pupils, as hollow outlines only. Ensure there are no solid black regions or shading. The lines are precise and appear machine-drawn for direct path tracing.",
        "2. 정밀한 얼굴 캐리커처": "A highly detailed black ink line art focusing on facial features and expressions. Pure black lines on a clean white background. Strictly NO SOLID FILLS. Eyes and pupils must be rendered as clean, hollow circular outlines with no solid color inside. The drawing must consist entirely of empty closed loops and paths for precise portrait plotting.",
        "3. 미니멀리스트 (최소한의 선)": "An extreme minimalist line drawing using the absolute minimum number of continuous black lines to represent the person's character. Strictly no solid fills or shading. Represent eyes and pupils as simple hollow shapes without filling them. Only pure black outlines on a white background. Very clean for fast plotting.",
        "4. 굵은 코믹스 외곽선": "Bold and strong black outlines, comic book style line art. Use only outlines to define shapes. Do not use solid fills for shadows, hair, or features. Eyes and pupils must be rendered as hollow line drawings with no solid fill. No solid black regions. High contrast but composed entirely of empty paths."
    }
    return _load_json_prompts(PROMPTS_FILE, default_prompts)

def load_character_prompts():
    default_char_prompts = {
        "1. 어깨 위의 파트너": "A pure black line art caricature of the person from the first image with the character from the second image sitting naturally on their shoulder. They are in the same scene, interacting. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients. Hollow eyes. Machine-drawn style for plotting.",
        "2. 나란히 서 있는 친구": "A pure black line art caricature of the person from the first image standing side-by-side with the character from the second image as friends. Draw them interacting naturally. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients. Hollow eyes.",
        "3. 머리 위의 요정": "A pure black line art caricature of the person from the first image with the small character from the second image sitting or floating above their head like a fairy. Draw the entire scene exclusively with lines of exactly the same thickness (uniform line weight) using solid black ink. No solid fills, shading, or gradients.",
        "4. 함께 손을 흔드는 모습": "A pure black line art caricature of the person from the first image and the character from the second image standing together and waving their hands at the viewer. Both are in the same line art style, rendered exclusively with lines of exactly the same thickness using solid black ink."
    }
    return _load_json_prompts(CHAR_PROMPTS_FILE, default_char_prompts)

# --- 세션 관리 ---
# 프로그램의 단일 실행 인스턴스 동안 유지되는 최상위 세션 폴더 경로
SESSION_DIR = None

def initialize_session():
    """
    프로그램 실행 시 단 한 번만 호출되어 메인 세션 폴더를 생성합니다.
    이 함수는 생성된 최상위 세션 폴더의 경로를 반환합니다.
    """
    global SESSION_DIR
    if SESSION_DIR is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        session_folder_name = f"{timestamp}_session"
        SESSION_DIR = os.path.join(DATA_DIR, session_folder_name)
        os.makedirs(SESSION_DIR, exist_ok=True)
        print(f"[세션 초기화] 메인 세션 폴더가 생성되었습니다: {SESSION_DIR}")
    return SESSION_DIR

def setup_photo_paths(photo_name="photo"):
    """
    메인 세션 폴더 아래에 개별 사진 처리를 위한 하위 폴더
    (raw, intermediate, processed)를 생성하고 각 경로를 반환합니다.
    """
    if SESSION_DIR is None:
        raise RuntimeError("세션이 초기화되지 않았습니다. initialize_session()을 먼저 호출해야 합니다.")

    photo_folder_path = os.path.join(SESSION_DIR, photo_name)

    # 개별 사진 폴더 내의 하위 폴더 경로 설정
    input_dir = os.path.join(photo_folder_path, "raw")
    intermediate_dir = os.path.join(photo_folder_path, "intermediate")
    output_dir = os.path.join(photo_folder_path, "processed")

    # 모든 폴더 생성
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(intermediate_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    print(f"  - 사진 처리 폴더를 생성했습니다: {photo_folder_path}")
    return input_dir, intermediate_dir, output_dir

# --- 고정 설정값 ---
# Canny 엣지 설정
FINAL_TH1 = 50
FINAL_TH2 = 100

# G-코드(로봇) 설정 및 펜 설정 클래스
class PenConfig:
    def __init__(self, name, z_safe=10.0, z_draw=0.0, feed_rate=1000, scale=0.2):
        self.name = name
        self.z_safe = z_safe
        self.z_draw = z_draw
        self.feed_rate = feed_rate
        self.scale = scale

    def __str__(self):
        return self.name

# 기본 펜 설정 프리셋
PEN_PRESETS = {
    "네임펜": PenConfig("네임펜", z_safe=10.0, z_draw=0.0, feed_rate=1000, scale=0.2),
    "볼펜": PenConfig("볼펜", z_safe=10.0, z_draw=-0.5, feed_rate=800, scale=0.2),
    "마카": PenConfig("마카", z_safe=10.0, z_draw=0.5, feed_rate=1000, scale=0.2),
}

# 하위 호환성을 위한 기본값 유지
Z_SAFE = PEN_PRESETS["네임펜"].z_safe
Z_DRAW = PEN_PRESETS["네임펜"].z_draw
FEED_RATE = PEN_PRESETS["네임펜"].feed_rate
SCALE = PEN_PRESETS["네임펜"].scale

# 출력 도형 물리 크기 정규화(mm)
# 경로의 bbox를 아래 박스 안에 맞추고, 비율은 유지합니다.
TARGET_DRAW_WIDTH_MM = 100.0
TARGET_DRAW_HEIGHT_MM = 100.0
