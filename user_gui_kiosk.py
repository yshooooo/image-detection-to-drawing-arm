import sys
import os
import cv2
import numpy as np
import time
import subprocess
import traceback
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QProgressBar, 
                             QMessageBox, QFrame, QGridLayout, QSizePolicy,
                             QStackedWidget, QScrollArea)
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer, QSize
from PyQt6.QtGui import QImage, QPixmap, QFont, QPainter, QColor, QIcon

# Existing modules
from modules import config
from modules.sketch_processor import SketchProcessor

PEN_TCP_ARG_MAP = {
    "볼펜": "pen",
    "네임펜": "name",
    "마카": "maka",
}

# Reuse CameraThread and WorkerThread (same as basic)
# ... (CameraThread and WorkerThread omitted for brevity, will remain in file)
class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    status_signal = pyqtSignal(str)

    def __init__(self, source=0):
        super().__init__()
        self.source = source
        self._run_flag = True

    def run(self):
        try:
            source = int(self.source)
        except (TypeError, ValueError):
            source = self.source

        cap = cv2.VideoCapture(source)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        fail_count = 0

        while self._run_flag:
            ret, frame = cap.read()
            if ret and frame is not None and frame.size > 0:
                fail_count = 0
                h, w = frame.shape[:2]
                if w >= h * 1.8:
                    frame = frame[:, :w//2]
                self.change_pixmap_signal.emit(frame)
            else:
                fail_count += 1
                if fail_count == 1:
                    self.status_signal.emit(f"카메라 프레임 수신 실패(source={source})")
                if fail_count >= 30:
                    self.status_signal.emit("카메라 재연결 시도 중...")
                    cap.release()
                    time.sleep(0.3)
                    cap = cv2.VideoCapture(source)
                    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                    fail_count = 0
                time.sleep(0.03)

        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class WorkerThread(QThread):
    progress_signal = pyqtSignal(str, np.ndarray, str)
    finished_signal = pyqtSignal(list)
    error_signal = pyqtSignal(str)
    def __init__(self, processor, image, sketch_type, gemini_api_key=None, 
                 gemini_prompt=None, character_image=None, pen_config=None, temperature=0.0):
        super().__init__()
        self.processor = processor
        self.image = image
        self.sketch_type = sketch_type
        self.gemini_api_key = gemini_api_key
        self.gemini_prompt = gemini_prompt
        self.character_image = character_image
        self.pen_config = pen_config
        self.temperature = temperature
    def run(self):
        try:
            results = self.processor.process(
                self.image, self.sketch_type, self.gemini_api_key, 
                self.gemini_prompt, self.character_image, self.pen_config,
                progress_callback=self.emit_progress,
                temperature=self.temperature
            )
            self.finished_signal.emit(results if results else [])
        except Exception as e:
            self.error_signal.emit(f"{e}\n\n{traceback.format_exc()}")
    def emit_progress(self, step_id, image, message):
        img = image if image is not None else np.array([], dtype=np.uint8)
        self.progress_signal.emit(step_id, img, message)

class RobotDrawingThread(QThread):
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, robot_script, nc_path, pen_arg):
        super().__init__()
        self.robot_script = robot_script
        self.nc_path = nc_path
        self.pen_arg = pen_arg

    def run(self):
        try:
            subprocess.run(
                [sys.executable, self.robot_script, self.nc_path, self.pen_arg],
                check=True
            )
            self.finished_signal.emit(True, "")
        except Exception as exc:
            self.finished_signal.emit(False, str(exc))

class KioskUserGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 포토부스 - 키오스크 모드")
        
        self.processor = SketchProcessor()
        self.current_frame = None
        self.captured_image = None
        self.prompts_dict = config.load_prompts()
        self.char_prompts_dict = config.load_character_prompts()
        self.portrait_preview_files = {
            name: f"portrait_style_{idx}.png"
            for idx, name in enumerate(self.prompts_dict.keys(), start=1)
        }
        self.char_action_indices = {
            name: idx
            for idx, name in enumerate(self.char_prompts_dict.keys(), start=1)
        }
        self.character_files = self.load_character_files()
        self.default_pen = config.PEN_PRESETS["네임펜"]
        self.selected_pen_name = "네임펜"
        self.selected_pen_config = self.default_pen
        self.api_key = "AIzaSyAAepYJsbdwtrVseJe3pqf0hKfvRz_yk1w"
        
        # State variables for selection
        self.selected_sketch_type = None
        self.selected_prompt = None
        self.selected_char_filename = None
        self.selected_char_img = None
        self.selected_prompt_name = None
        
        self.countdown_val = 0
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        
        self.reset_timer = QTimer()
        self.reset_timer.setSingleShot(True)
        self.reset_timer.timeout.connect(self.reset_to_standby)
        
        self.preview_dir = os.path.join(config.DATA_DIR, "preview")
        if not os.path.exists(self.preview_dir):
            os.makedirs(self.preview_dir, exist_ok=True)
        
        self.init_ui()
        self.showMaximized()
        self.start_camera()

    def load_character_files(self):
        if not os.path.exists(config.CHARACTERS_DIR):
            return []
        return sorted([
            f for f in os.listdir(config.CHARACTERS_DIR)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ])

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)
        
        # Create Pages
        self.page_camera = self.create_page_camera()      # State 1
        self.page_approval = self.create_page_approval()  # State 2
        self.page_pen = self.create_page_pen()            # State 3
        self.page_mode = self.create_page_mode()          # State 4
        self.page_portrait = self.create_page_portrait()  # State 5A
        self.page_char = self.create_page_char()          # State 5B
        self.page_result = self.create_page_result()      # State 6
        
        self.stack.addWidget(self.page_camera)
        self.stack.addWidget(self.page_approval)
        self.stack.addWidget(self.page_pen)
        self.stack.addWidget(self.page_mode)
        self.stack.addWidget(self.page_portrait)
        self.stack.addWidget(self.page_char)
        self.stack.addWidget(self.page_result)
        
        self.stack.setCurrentWidget(self.page_camera)

    def create_page_camera(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        label = QLabel("카메라 앞에 서주세요!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 45px; font-weight: bold; color: #333; margin: 15px;")
        layout.addWidget(label)

        self.camera_container = QFrame()
        self.camera_container.setStyleSheet("background-color: black; border-top: 3px solid #2196F3; border-bottom: 3px solid #2196F3;")
        cam_grid = QGridLayout(self.camera_container)
        cam_grid.setContentsMargins(0,0,0,0)
        
        self.camera_label = QLabel()
        self.camera_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.camera_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.camera_label.setScaledContents(False)
        cam_grid.addWidget(self.camera_label, 0, 0)
        
        self.overlay_label = QLabel("")
        self.overlay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_label.setStyleSheet("color: white; font-size: 300px; font-weight: bold; background: transparent;")
        cam_grid.addWidget(self.overlay_label, 0, 0)
        
        layout.addWidget(self.camera_container, stretch=1)
        
        btn_capture = QPushButton("사진 촬영")
        btn_capture.setFixedHeight(120)
        btn_capture.setStyleSheet("background-color: #F44336; color: white; font-size: 40px; font-weight: bold;")
        btn_capture.clicked.connect(self.start_countdown)
        layout.addWidget(btn_capture)
        
        return page

    def create_page_approval(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        label = QLabel("이 사진으로 진행할까요?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 45px; font-weight: bold; margin: 15px;")
        layout.addWidget(label)
        
        self.approval_img_label = QLabel()
        self.approval_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.approval_img_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.approval_img_label.setStyleSheet("background-color: black; border-top: 3px solid #4CAF50; border-bottom: 3px solid #4CAF50;")
        layout.addWidget(self.approval_img_label, stretch=1)
        
        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(20, 20, 20, 20)
        btn_layout.setSpacing(20)
        
        btn_retake = QPushButton("다시 촬영")
        btn_retake.setFixedHeight(100)
        btn_retake.setStyleSheet("background-color: #757575; color: white; font-size: 35px; font-weight: bold; border-radius: 10px;")
        btn_retake.clicked.connect(self.retake_photo)
        
        btn_approve = QPushButton("이 사진 사용하기")
        btn_approve.setFixedHeight(100)
        btn_approve.setStyleSheet("background-color: #4CAF50; color: white; font-size: 35px; font-weight: bold; border-radius: 10px;")
        btn_approve.clicked.connect(self.go_to_pen_selection)
        
        btn_layout.addWidget(btn_retake)
        btn_layout.addWidget(btn_approve)
        layout.addLayout(btn_layout)
        
        return page

    def create_page_pen(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        label = QLabel("사용할 펜을 선택해주세요")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 40px; font-weight: bold; margin: 20px;")
        layout.addWidget(label)

        self.pen_selected_label = QLabel("")
        self.pen_selected_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pen_selected_label.setStyleSheet("font-size: 24px; color: #555;")
        layout.addWidget(self.pen_selected_label)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(25)
        colors = ["#455A64", "#1976D2", "#E65100"]

        for idx, pen_name in enumerate(config.PEN_PRESETS.keys()):
            btn = QPushButton(pen_name)
            btn.setFixedSize(280, 220)
            btn.setStyleSheet(
                f"background-color: {colors[idx % len(colors)]}; color: white; "
                "font-size: 34px; font-weight: bold; border-radius: 20px;"
            )
            btn.clicked.connect(lambda checked, name=pen_name: self.select_pen(name))
            btn_layout.addWidget(btn)

        layout.addStretch()
        layout.addLayout(btn_layout)
        layout.addStretch()

        btn_back = QPushButton("뒤로 가기")
        btn_back.setFixedSize(220, 70)
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_approval))
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

        return page

    def create_page_mode(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        label = QLabel("모드를 선택해주세요")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 40px; font-weight: bold; margin: 50px;")
        layout.addWidget(label)
        
        btn_layout = QHBoxLayout()
        btn_portrait = QPushButton("🎨 초상화\n(캐리커처)")
        btn_portrait.setFixedSize(400, 300)
        btn_portrait.setStyleSheet("background-color: #2196F3; color: white; font-size: 40px; border-radius: 20px;")
        btn_portrait.clicked.connect(self.go_to_portrait_mode)
        
        btn_char = QPushButton("🐾 캐릭터\n동반 모드")
        btn_char.setFixedSize(400, 300)
        btn_char.setStyleSheet("background-color: #FF9800; color: white; font-size: 40px; border-radius: 20px;")
        btn_char.clicked.connect(self.go_to_char_mode)
        
        btn_layout.addStretch()
        btn_layout.addWidget(btn_portrait)
        btn_layout.addSpacing(50)
        btn_layout.addWidget(btn_char)
        btn_layout.addStretch()
        
        layout.addLayout(btn_layout)
        layout.addStretch()
        
        btn_back = QPushButton("뒤로 가기")
        btn_back.setFixedSize(200, 60)
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_pen))
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignCenter)
        
        return page

    def create_page_portrait(self):
        page = QWidget()
        layout = QHBoxLayout(page)
        
        # Left: Preview
        self.portrait_preview = QLabel()
        self.portrait_preview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.portrait_preview.setStyleSheet("border: 3px solid #ccc; background-color: #eee;")
        self.portrait_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.portrait_preview, stretch=1)
        
        # Right: Prompts
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        label = QLabel("스타일을 선택하세요")
        label.setStyleSheet("font-size: 30px; font-weight: bold;")
        right_layout.addWidget(label)
        
        self.portrait_btn_group = QWidget()
        self.portrait_grid = QGridLayout(self.portrait_btn_group)
        
        colors = ["#F44336", "#4CAF50", "#FFC107", "#9C27B0"]
        for i, (name, prompt) in enumerate(self.prompts_dict.items()):
            btn = QPushButton(name.split(".")[-1].strip())
            btn.setFixedSize(200, 100)
            color = colors[i % len(colors)]
            btn.setStyleSheet(f"background-color: {color}; color: white; font-size: 18px; font-weight: bold; border-radius: 10px;")
            btn.clicked.connect(lambda checked, p=prompt, n=name: self.select_portrait_prompt(p, n))
            self.portrait_grid.addWidget(btn, i // 2, i % 2)
            
        portrait_scroll = QScrollArea()
        portrait_scroll.setWidgetResizable(True)
        portrait_scroll.setWidget(self.portrait_btn_group)
        right_layout.addWidget(portrait_scroll)
        right_layout.addStretch()
        
        self.btn_start_portrait = QPushButton("생성 시작")
        self.btn_start_portrait.setFixedHeight(80)
        self.btn_start_portrait.setEnabled(False)
        self.btn_start_portrait.setStyleSheet("background-color: #2196F3; color: white; font-size: 25px; font-weight: bold;")
        self.btn_start_portrait.clicked.connect(self.start_generation)
        right_layout.addWidget(self.btn_start_portrait)
        
        btn_back = QPushButton("이전으로")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_mode))
        right_layout.addWidget(btn_back)
        
        layout.addWidget(right_widget, stretch=1)
        return page

    def create_page_char(self):
        page = QWidget()
        layout = QHBoxLayout(page)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(24)
        
        # Left: Preview
        self.char_preview = QLabel()
        self.char_preview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.char_preview.setStyleSheet("border: 4px solid #F9A826; background-color: #1e1e1e; border-radius: 20px;")
        self.char_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.char_preview, stretch=2)
        
        # Right
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(10, 10, 10, 10)
        right_layout.setSpacing(18)
        
        # Characters
        label_char = QLabel("1. 캐릭터 선택")
        label_char.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        right_layout.addWidget(label_char)
        
        char_scroll = QScrollArea()
        char_scroll.setFixedHeight(180)
        char_scroll.setWidgetResizable(True)
        char_container = QWidget()
        char_container.setStyleSheet("background: transparent;")
        char_layout = QHBoxLayout(char_container)
        char_layout.setSpacing(12)
        
        for f in self.character_files:
            char_path = os.path.join(config.CHARACTERS_DIR, f)
            btn = QPushButton()
            btn.setFixedSize(140, 140)
            
            # Load and set character image on button
            img_array = np.fromfile(char_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
            if img is not None:
                pixmap = self.frame_to_pixmap(img)
                btn.setIcon(QIcon(pixmap))
                btn.setIconSize(QSize(120, 120))
            
            btn.setStyleSheet("background-color: #607D8B; border-radius: 15px; border: 2px solid #455A64;")
            btn.clicked.connect(lambda checked, img=f: self.select_character(img))
            char_layout.addWidget(btn)
        char_scroll.setWidget(char_container)
        right_layout.addWidget(char_scroll)
        
        # Prompts (Action styles)
        label_prompt = QLabel("2. 동반 스타일 선택")
        label_prompt.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        right_layout.addWidget(label_prompt)
        
        prompt_scroll = QScrollArea()
        prompt_scroll.setWidgetResizable(True)
        prompt_container = QWidget()
        prompt_container.setStyleSheet("background: transparent;")
        prompt_grid = QGridLayout(prompt_container)
        prompt_grid.setSpacing(12)
        
        colors = ["#78909C", "#5C6BC0", "#26A69A", "#42A5F5"]
        
        for i, (name, prompt) in enumerate(self.char_prompts_dict.items()):
            btn = QPushButton(name)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            color = colors[i % len(colors)]
            btn.setStyleSheet(f"background-color: {color}; color: white; font-size: 20px; font-weight: bold; border-radius: 12px; padding: 10px;")
            btn.clicked.connect(lambda checked, p=prompt, n=name: self.select_char_prompt(p, n))
            prompt_grid.addWidget(btn, i // 2, i % 2)
            
        prompt_scroll.setWidget(prompt_container)
        right_layout.addWidget(prompt_scroll, stretch=1)
        
        self.btn_start_char = QPushButton("생성 시작")
        self.btn_start_char.setFixedHeight(80)
        self.btn_start_char.setEnabled(False)
        self.btn_start_char.setStyleSheet("background-color: #FF9800; color: white; font-size: 28px; font-weight: bold; border-radius: 15px;")
        self.btn_start_char.clicked.connect(self.start_generation)
        right_layout.addWidget(self.btn_start_char)
        
        btn_back = QPushButton("이전으로")
        btn_back.setFixedHeight(60)
        btn_back.setStyleSheet("background-color: #757575; color: white; font-size: 22px; font-weight: bold; border-radius: 12px;")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_mode))
        right_layout.addWidget(btn_back)
        
        layout.addWidget(right_widget, stretch=3)
        return page

    def create_page_result(self):
        page = QWidget()
        layout = QHBoxLayout(page)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        
        # Left: Original
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_title = QLabel("원본 사진")
        left_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_title.setStyleSheet("font-size: 22px; font-weight: bold;")
        left_layout.addWidget(left_title)
        self.result_orig_label = QLabel()
        self.result_orig_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_orig_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.result_orig_label.setMinimumSize(400, 500)
        self.result_orig_label.setStyleSheet("border: 5px solid #4CAF50; background-color: #1e1e1e;")
        left_layout.addWidget(self.result_orig_label, stretch=1)
        layout.addWidget(left_widget, stretch=1)
        
        self.result_arrow_label = QLabel("→")
        self.result_arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_arrow_label.setFixedWidth(80)
        self.result_arrow_label.setStyleSheet("font-size: 64px; font-weight: bold; color: white;")
        layout.addWidget(self.result_arrow_label)
        
        # Right: Result
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        self.result_title = QLabel("AI가 그림을 그리고 있습니다...")
        self.result_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_title.setStyleSheet("font-size: 25px; font-weight: bold;")
        right_layout.addWidget(self.result_title)
        
        self.result_img_label = QLabel()
        self.result_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_img_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.result_img_label.setMinimumSize(400, 500)
        self.result_img_label.setStyleSheet("border: 5px solid #2196F3; background-color: #1e1e1e;")
        right_layout.addWidget(self.result_img_label, stretch=1)
        
        self.result_progress = QProgressBar()
        self.result_progress.setFixedHeight(30)
        right_layout.addWidget(self.result_progress)
        
        layout.addWidget(right_widget, stretch=1)
        return page

    def frame_to_rgb(self, image):
        if image is None or image.size == 0:
            return None

        if image.ndim == 2:
            return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

        channels = image.shape[2]
        if channels == 1:
            return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        if channels == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if channels == 4:
            return cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)

        raise ValueError(f"지원하지 않는 이미지 채널 수: {channels}")

    def frame_to_pixmap(self, image):
        rgb_image = self.frame_to_rgb(image)
        if rgb_image is None:
            return QPixmap()

        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
        return QPixmap.fromImage(qt_image)

    def safe_filename_part(self, value):
        stem = os.path.splitext(os.path.basename(value))[0]
        invalid_chars = '<>:"/\\|?*'
        safe = ''.join('_' if c in invalid_chars or c.isspace() else c for c in stem)
        return safe.strip('._') or 'character'

    def portrait_preview_path(self, prompt_name):
        candidates = [
            os.path.join(self.preview_dir, f"portrait_{self.safe_filename_part(prompt_name)}.png")
        ]
        filename = self.portrait_preview_files.get(prompt_name)
        if filename:
            candidates.append(os.path.join(self.preview_dir, filename))
        return self.first_existing_path(candidates)

    def character_preview_path(self, character_filename, prompt_name):
        action_idx = self.char_action_indices.get(prompt_name)
        if not character_filename or not prompt_name:
            return None
        character_name = self.safe_filename_part(character_filename)
        candidates = [
            os.path.join(self.preview_dir, f"character_{character_name}_action_{self.safe_filename_part(prompt_name)}.png")
        ]
        if action_idx is not None:
            candidates.append(os.path.join(self.preview_dir, f"character_{character_name}_action_{action_idx}.png"))
        return self.first_existing_path(candidates)

    def first_existing_path(self, paths):
        for path in paths:
            if path and os.path.exists(path):
                return path
        return paths[0] if paths else None

    def show_preview_file(self, label_widget, image_path, missing_message=None):
        label_widget.clear()
        label_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_widget.setWordWrap(True)

        if not image_path or not os.path.exists(image_path):
            message = missing_message or "프리뷰 이미지를 선택해 주세요."
            label_widget.setText(message)
            return

        img_array = np.fromfile(image_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
        if image is None:
            label_widget.setText(f"프리뷰 이미지를 읽을 수 없습니다.\n{image_path}")
            return

        pixmap = self.frame_to_pixmap(image)
        target_size = label_widget.size()
        if target_size.width() < 100 or target_size.height() < 100:
            target_size = self.stack.size()
        label_widget.setPixmap(pixmap.scaled(
            target_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    def refresh_character_preview(self):
        image_path = self.character_preview_path(self.selected_char_filename, self.selected_prompt_name)
        if image_path:
            self.show_preview_file(
                self.char_preview,
                image_path,
                f"프리뷰 이미지 없음\n{image_path}"
            )
        else:
            self.char_preview.setWordWrap(True)
            self.char_preview.setText("캐릭터와 동작을 선택하면\n조합별 프리뷰가 표시됩니다.")

    def start_camera(self):
        if hasattr(self, 'camera_thread') and self.camera_thread.isRunning():
            self.camera_thread.stop()
        self.camera_thread = CameraThread(source=0)
        self.camera_thread.change_pixmap_signal.connect(self.update_camera_feed)
        self.camera_thread.status_signal.connect(lambda message: print(f"[Camera] {message}"))
        self.camera_thread.start()

    def update_camera_feed(self, frame):
        if frame is None or frame.size == 0:
            return

        if self.captured_image is None:
            self.current_frame = frame.copy()
            self.display_scaled_image(self.camera_label, frame, fallback_widget=self.camera_container)

    def display_scaled_image(self, label_widget, image, fallback_widget=None):
        pixmap = self.frame_to_pixmap(image)
        target_size = label_widget.size()

        if target_size.width() < 100 or target_size.height() < 100:
            fallback = fallback_widget if fallback_widget is not None else self.stack
            target_size = fallback.size()

        if target_size.width() <= 0 or target_size.height() <= 0:
            return

        label_widget.setPixmap(pixmap.scaled(
            target_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    def start_countdown(self):
        if self.countdown_timer.isActive():
            return
        if self.current_frame is None or self.current_frame.size == 0:
            QMessageBox.warning(self, "카메라 오류", "촬영할 카메라 화면이 아직 준비되지 않았습니다.")
            return

        self.countdown_val = 3
        self.overlay_label.setText(str(self.countdown_val))
        self.countdown_timer.start(1000)

    def update_countdown(self):
        self.countdown_val -= 1
        if self.countdown_val > 0:
            self.overlay_label.setText(str(self.countdown_val))
        else:
            self.countdown_timer.stop()
            self.overlay_label.setText("")
            self.capture_image()

    def capture_image(self):
        if self.current_frame is None or self.current_frame.size == 0:
            QMessageBox.warning(self, "카메라 오류", "촬영할 카메라 화면이 없습니다. 카메라 연결을 확인해 주세요.")
            return

        self.captured_image = self.current_frame.copy()
        
        # Update approval page
        pixmap = self.frame_to_pixmap(self.captured_image)
        
        # Use stack size as target if label size is not yet established
        target_size = self.approval_img_label.size()
        if target_size.width() < 100: target_size = self.stack.size()
        
        pixmap = pixmap.scaled(
            target_size, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.approval_img_label.setPixmap(pixmap)
        self.stack.setCurrentWidget(self.page_approval)

    def retake_photo(self):
        self.countdown_timer.stop()
        self.overlay_label.setText("")
        self.captured_image = None
        self.approval_img_label.clear()
        self.selected_pen_name = "네임펜"
        self.selected_pen_config = self.default_pen
        self.stack.setCurrentWidget(self.page_camera)

    def go_to_pen_selection(self):
        self.selected_pen_name = "네임펜"
        self.selected_pen_config = self.default_pen
        self.pen_selected_label.setText(f"현재 선택: {self.selected_pen_name}")
        self.stack.setCurrentWidget(self.page_pen)

    def select_pen(self, pen_name):
        self.selected_pen_name = pen_name
        self.selected_pen_config = config.PEN_PRESETS[pen_name]
        self.pen_selected_label.setText(f"현재 선택: {pen_name}")
        self.stack.setCurrentWidget(self.page_mode)

    def go_to_portrait_mode(self):
        self.selected_sketch_type = "GEMINI"
        self.selected_prompt = None
        self.selected_prompt_name = None
        self.btn_start_portrait.setEnabled(False)
        self.stack.setCurrentWidget(self.page_portrait)
        QTimer.singleShot(
            100,
            lambda: (
                self.portrait_preview.setWordWrap(True),
                self.portrait_preview.setText("스타일을 선택하면\n해당 프리뷰가 표시됩니다.")
            )
        )

    def go_to_char_mode(self):
        self.selected_sketch_type = "GEMINI_CHAR"
        self.selected_prompt = None
        self.selected_prompt_name = None
        self.selected_char_filename = None
        self.selected_char_img = None
        self.btn_start_char.setEnabled(False)
        self.stack.setCurrentWidget(self.page_char)
        QTimer.singleShot(100, self.refresh_character_preview)

    def update_preview(self, label_widget, overlay_img=None, overlay_text=None):
        if self.captured_image is None: return
        
        base_pixmap = self.frame_to_pixmap(self.captured_image)
        
        target_size = label_widget.size()
        if target_size.width() < 100: target_size = self.stack.size()
        
        pixmap = base_pixmap.scaled(
            target_size, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        if overlay_img is not None or overlay_text is not None:
            painter = QPainter(pixmap)
            if overlay_img is not None:
                # Draw character overlay
                ov_pix = self.frame_to_pixmap(overlay_img).scaled(
                    pixmap.width() // 4, pixmap.height() // 4, 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                painter.drawPixmap(pixmap.width() - ov_pix.width() - 10, pixmap.height() - ov_pix.height() - 10, ov_pix)
            
            if overlay_text:
                painter.setPen(QColor(255, 255, 255))
                painter.setFont(QFont("Arial", pixmap.height() // 20, QFont.Weight.Bold))
                painter.drawText(20, pixmap.height() // 10, f"스타일: {overlay_text}")
            painter.end()
            
        label_widget.setPixmap(pixmap)

    def select_portrait_prompt(self, prompt, name):
        self.selected_prompt = prompt
        self.selected_prompt_name = name
        image_path = self.portrait_preview_path(name)
        self.show_preview_file(
            self.portrait_preview,
            image_path,
            f"프리뷰 이미지 없음\n{image_path}"
        )
        self.btn_start_portrait.setEnabled(True)

    def select_character(self, filename):
        self.selected_char_filename = filename
        char_path = os.path.join(config.CHARACTERS_DIR, filename)
        img_array = np.fromfile(char_path, np.uint8)
        self.selected_char_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if self.selected_char_img is None:
            QMessageBox.warning(self, "캐릭터 오류", f"캐릭터 이미지를 읽을 수 없습니다.\n{char_path}")
            self.selected_char_filename = None
            self.btn_start_char.setEnabled(False)
            return
        self.refresh_character_preview()
        if self.selected_prompt:
            self.btn_start_char.setEnabled(True)

    def select_char_prompt(self, prompt, name):
        self.selected_prompt = prompt
        self.selected_prompt_name = name
        self.refresh_character_preview()
        if self.selected_char_filename:
            self.btn_start_char.setEnabled(True)

    def start_generation(self):
        self.reset_timer.stop()
        if self.captured_image is None:
            QMessageBox.warning(self, "이미지 오류", "촬영된 사진이 없습니다.")
            return
        if not self.selected_prompt:
            QMessageBox.warning(self, "선택 오류", "스타일 또는 동작을 선택해 주세요.")
            return
        if self.selected_sketch_type == "GEMINI_CHAR" and self.selected_char_img is None:
            QMessageBox.warning(self, "선택 오류", "캐릭터를 선택해 주세요.")
            return

        # Prepare result page
        self.stack.setCurrentWidget(self.page_result)
        QApplication.processEvents()

        pixmap = self.frame_to_pixmap(self.captured_image)
        
        target_size = self.result_orig_label.size()
        if target_size.width() < 100 or target_size.height() < 100:
            target_size = self.result_orig_label.minimumSize()
        
        self.result_orig_label.setPixmap(pixmap.scaled(
            target_size, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        ))
        
        self.result_title.setText("AI가 그림을 그리고 있습니다...")
        self.result_progress.setRange(0, 0)
        self.result_img_label.clear()
        
        if not self.api_key:
            QMessageBox.critical(self, "오류", "API Key가 없습니다.")
            self.reset_to_standby()
            return

        self.worker = WorkerThread(
            SketchProcessor(), self.captured_image, self.selected_sketch_type,
            gemini_api_key=self.api_key, gemini_prompt=self.selected_prompt,
            character_image=self.selected_char_img, pen_config=self.selected_pen_config,
            temperature=0.0
        )
        self.worker.progress_signal.connect(self.on_worker_progress)
        self.worker.finished_signal.connect(self.on_worker_finished)
        self.worker.error_signal.connect(self.on_worker_error)
        self.worker.start()

    def on_worker_progress(self, step_id, image, message):
        if image.size > 0 and (step_id == "sketch" or step_id == "done"):
            base_pixmap = self.frame_to_pixmap(image)
            
            target_size = self.result_img_label.size()
            if target_size.width() < 100 or target_size.height() < 100:
                target_size = self.result_img_label.minimumSize()
            
            pixmap = base_pixmap.scaled(
                target_size, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )
            self.result_img_label.setPixmap(pixmap)

    def on_worker_finished(self, results):
        self.result_progress.setRange(0, 100)
        self.result_progress.setValue(100)
        if results:
            nc_path = results[0]
            self.result_title.setText("로봇이 그림을 그리고 있습니다. 완료될 때까지 잠시만 기다려주세요.")
            self.run_robot_drawing(nc_path)
        else:
            self.result_title.setText("그리기에 실패했습니다. 다시 시도해주세요.")
            self.reset_timer.start(15000)

    def on_worker_error(self, err_msg):
        self.result_progress.setRange(0, 100)
        self.result_title.setText(f"오류 발생: {err_msg}")
        self.reset_timer.start(5000)

    def run_robot_drawing(self, nc_path):
        robot_script = os.path.join(os.path.dirname(__file__), "modules", "fianl_drawing_robot.py")
        pen_arg = PEN_TCP_ARG_MAP.get(self.selected_pen_name, "pen")
        self.robot_thread = RobotDrawingThread(robot_script, nc_path, pen_arg)
        self.robot_thread.finished_signal.connect(self.on_robot_drawing_finished)
        self.robot_thread.start()

    def on_robot_drawing_finished(self, success, error_message):
        if success:
            self.result_title.setText("로봇 그리기가 완료되었습니다. 잠시 후 처음 화면으로 돌아갑니다.")
            self.reset_timer.start(5000)
            return

        self.result_title.setText(f"로봇 실행 오류: {error_message}")
        self.reset_timer.start(10000)

    def reset_to_standby(self):
        self.captured_image = None
        self.selected_sketch_type = None
        self.selected_prompt = None
        self.selected_char_filename = None
        self.selected_char_img = None
        self.selected_prompt_name = None
        self.selected_pen_name = "네임펜"
        self.selected_pen_config = self.default_pen
        self.btn_start_portrait.setEnabled(False)
        self.btn_start_char.setEnabled(False)
        self.stack.setCurrentWidget(self.page_camera)
        self.overlay_label.setText("")

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = KioskUserGui()
    gui.show()
    sys.exit(app.exec())
