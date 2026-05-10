import sys
import os
import cv2
import numpy as np
import time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QProgressBar, 
                             QMessageBox, QFrame, QGridLayout, QSizePolicy)
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap, QFont

# Existing modules
from modules import config
from modules.sketch_processor import SketchProcessor

# Reuse CameraThread and WorkerThread (same as basic)
class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self, source=0):
        super().__init__()
        self.source = source
        self._run_flag = True
    def run(self):
        cap = cv2.VideoCapture(self.source)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        while self._run_flag:
            ret, frame = cap.read()
            if ret:
                h, w = frame.shape[:2]
                if w >= h * 1.8: frame = frame[:, :w//2]
                self.change_pixmap_signal.emit(frame)
            else:
                time.sleep(0.1)
        cap.release()
    def stop(self):
        self._run_flag = False
        self.wait()

class WorkerThread(QThread):
    progress_signal = pyqtSignal(str, np.ndarray, str)
    finished_signal = pyqtSignal(list)
    error_signal = pyqtSignal(str)
    def __init__(self, processor, image, sketch_type, gemini_api_key=None, 
                 gemini_prompt=None, character_image=None, pen_config=None):
        super().__init__()
        self.processor = processor
        self.image = image
        self.sketch_type = sketch_type
        self.gemini_api_key = gemini_api_key
        self.gemini_prompt = gemini_prompt
        self.character_image = character_image
        self.pen_config = pen_config
    def run(self):
        try:
            results = self.processor.process(
                self.image, self.sketch_type, self.gemini_api_key, 
                self.gemini_prompt, self.character_image, self.pen_config,
                progress_callback=self.emit_progress
            )
            self.finished_signal.emit(results if results else [])
        except Exception as e:
            self.error_signal.emit(str(e))
    def emit_progress(self, step_id, image, message):
        img = image if image is not None else np.array([], dtype=np.uint8)
        self.progress_signal.emit(step_id, img, message)

class KioskUserGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 포토부스 - 키오스크 모드")
        
        self.processor = SketchProcessor()
        self.current_frame = None
        self.captured_image = None
        self.prompts_dict = config.load_prompts()
        self.default_pen = config.PEN_PRESETS["네임펜"]
        self.api_key = "AIzaSyAAepYJsbdwtrVseJe3pqf0hKfvRz_yk1w" # 여기에 실제 API 키 입력
        
        self.countdown_val = 0
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        
        self.reset_timer = QTimer()
        self.reset_timer.setSingleShot(True)
        self.reset_timer.timeout.connect(self.reset_to_standby)
        
        self.init_ui()
        self.showMaximized()
        self.start_camera()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 1. 상단: 안내 메시지
        self.instruction_label = QLabel("원하는 스타일을 눌러주세요!")
        self.instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instruction_label.setStyleSheet("font-size: 40px; font-weight: bold; color: #333; margin: 20px;")
        self.main_layout.addWidget(self.instruction_label)

        # 2. 중앙: 카메라 레이아웃
        self.camera_container = QFrame()
        self.camera_container.setStyleSheet("background-color: black; border: 5px solid #2196F3; border-radius: 10px;")
        self.camera_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.cam_grid = QGridLayout(self.camera_container)
        self.cam_grid.setContentsMargins(0,0,0,0)
        
        self.camera_label = QLabel()
        self.camera_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.camera_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.cam_grid.addWidget(self.camera_label, 0, 0)
        
        # 카운트다운 오버레이
        self.overlay_label = QLabel("")
        self.overlay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_label.setStyleSheet("color: white; font-size: 200px; font-weight: bold; background: transparent;")
        self.overlay_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.cam_grid.addWidget(self.overlay_label, 0, 0)
        
        self.main_layout.addWidget(self.camera_container, stretch=1)

        # 3. 진행바
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedHeight(30)
        self.main_layout.addWidget(self.progress_bar)

        # 4. 하단: 스타일 및 캐릭터 버튼들
        self.button_container = QWidget()
        self.btn_layout = QHBoxLayout(self.button_container)
        self.btn_layout.setSpacing(20)
        
        # 일반 스타일 버튼
        colors = ["#F44336", "#4CAF50", "#FFC107", "#9C27B0"]
        for i, (name, prompt) in enumerate(self.prompts_dict.items()):
            btn = QPushButton(name.split(".")[-1].strip())
            btn.setFixedHeight(120)
            color = colors[i % len(colors)]
            btn.setStyleSheet(f"background-color: {color}; color: white; font-size: 20px; font-weight: bold; border-radius: 15px;")
            btn.clicked.connect(lambda checked, p=prompt: self.start_kiosk_flow("GEMINI", p))
            self.btn_layout.addWidget(btn)

        # 캐릭터 버튼 추가
        self.char_prompts_dict = config.load_character_prompts()
        if os.path.exists(config.CHARACTERS_DIR):
            char_files = [f for f in os.listdir(config.CHARACTERS_DIR) 
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for f in char_files:
                char_name = os.path.splitext(f)[0]
                btn = QPushButton(f"🐾 {char_name}")
                btn.setFixedHeight(120)
                btn.setStyleSheet("background-color: #607D8B; color: white; font-size: 20px; font-weight: bold; border-radius: 15px;")
                # 첫 번째 캐릭터 프롬프트를 기본으로 사용
                char_prompt = list(self.char_prompts_dict.values())[0]
                btn.clicked.connect(lambda checked, p=char_prompt, img=f: self.start_kiosk_flow("GEMINI_CHAR", p, img))
                self.btn_layout.addWidget(btn)
            
        self.main_layout.addWidget(self.button_container)

    def start_camera(self):
        self.camera_thread = CameraThread(source=0)
        self.camera_thread.change_pixmap_signal.connect(self.update_camera_feed)
        self.camera_thread.start()

    def update_camera_feed(self, frame):
        if self.captured_image is None:
            self.current_frame = frame
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch*w, QImage.Format.Format_RGB888).copy()
            pixmap = QPixmap.fromImage(qt_image)
            
            target_size = self.camera_container.size()
            if target_size.width() > 0 and target_size.height() > 0:
                scaled_pixmap = pixmap.scaled(target_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.camera_label.setPixmap(scaled_pixmap)

    def start_kiosk_flow(self, sketch_type, prompt, char_filename=None):
        self.selected_sketch_type = sketch_type
        self.selected_prompt = prompt
        self.selected_char_filename = char_filename
        
        self.button_container.setEnabled(False)
        self.instruction_label.setText("준비하세요!")
        
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
            self.capture_and_process()

    def capture_and_process(self):
        if self.current_frame is not None:
            self.captured_image = self.current_frame.copy()
            self.update_camera_feed(self.captured_image)
            
            self.instruction_label.setText("AI가 그림을 그리고 있습니다...")
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, 0)
            
            if not self.api_key:
                QMessageBox.critical(self, "오류", "API Key가 없습니다.")
                self.reset_to_standby()
                return

            character_image = None
            if self.selected_sketch_type == "GEMINI_CHAR" and self.selected_char_filename:
                char_path = os.path.join(config.CHARACTERS_DIR, self.selected_char_filename)
                img_array = np.fromfile(char_path, np.uint8)
                character_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            self.worker = WorkerThread(
                SketchProcessor(), self.captured_image, self.selected_sketch_type,
                gemini_api_key=self.api_key, gemini_prompt=self.selected_prompt,
                character_image=character_image, pen_config=self.default_pen
            )
            self.worker.progress_signal.connect(self.on_worker_progress)
            self.worker.finished_signal.connect(self.on_worker_finished)
            self.worker.error_signal.connect(self.on_worker_error)
            self.worker.start()

    def on_worker_progress(self, step_id, image, message):
        if image.size > 0 and (step_id == "sketch" or step_id == "done"):
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch*w, QImage.Format.Format_RGB888).copy()
            
            target_size = self.camera_container.size()
            scaled_pixmap = QPixmap.fromImage(qt_image).scaled(target_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.camera_label.setPixmap(scaled_pixmap)

    def on_worker_finished(self, results):
        self.progress_bar.setVisible(False)
        if results:
            nc_path = results[0]
            self.instruction_label.setText("로봇이 그리기를 시작합니다! 감사합니다.")
            self.run_robot_drawing(nc_path)
        else:
            self.instruction_label.setText("그리기에 실패했습니다. 다시 시도해주세요.")
        
        self.reset_timer.start(15000)

    def on_worker_error(self, err_msg):
        self.progress_bar.setVisible(False)
        self.instruction_label.setText(f"오류 발생: {err_msg}")
        self.reset_timer.start(5000)

    def run_robot_drawing(self, nc_path):
        import subprocess
        robot_script = os.path.join(os.path.dirname(__file__), "modules", "fianl_drawing_robot.py")
        try:
            subprocess.Popen([sys.executable, robot_script, nc_path, "pen"])
        except Exception:
            pass

    def reset_to_standby(self):
        self.captured_image = None
        self.button_container.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.instruction_label.setText("원하는 스타일을 눌러주세요!")
        self.overlay_label.setText("")

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = KioskUserGui()
    gui.show()
    sys.exit(app.exec())
