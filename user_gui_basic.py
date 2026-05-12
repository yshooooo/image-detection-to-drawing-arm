import sys
import os
import cv2
import numpy as np
import time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QComboBox, QPushButton, 
                             QProgressBar, QMessageBox)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap

# Existing modules
from modules import config
from modules.sketch_processor import SketchProcessor
from modules.human_cropper import detect_face_and_get_roi

# Reuse CameraThread and WorkerThread from gui_app.py
class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    status_signal = pyqtSignal(str)

    def __init__(self, source=0):
        super().__init__()
        self.source = source
        self._run_flag = True
        self._frame_count = 0
        self._last_face_roi = None
        self._detect_interval = 6

    def run(self):
        cap = cv2.VideoCapture(self.source)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        fail_count = 0
        while self._run_flag:
            ret, frame = cap.read()
            if ret:
                fail_count = 0
                self.process_and_emit(frame)
            else:
                fail_count += 1
                if fail_count >= 30:
                    self.status_signal.emit("카메라 재연결 시도 중...")
                    cap.release()
                    time.sleep(0.3)
                    cap = cv2.VideoCapture(self.source)
                    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                    fail_count = 0
        cap.release()

    def process_and_emit(self, frame):
        h, w = frame.shape[:2]
        if w >= h * 1.8: # ZED Side-by-Side 대응
            frame = frame[:, :w//2]
        self.change_pixmap_signal.emit(frame)

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
            self.error_signal.emit(f"처리 중 오류 발생: {str(e)}")

    def emit_progress(self, step_id, image, message):
        img_to_send = image if image is not None else np.array([], dtype=np.uint8)
        self.progress_signal.emit(step_id, img_to_send, message)

class BasicUserGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 스케치 - 사용자 모드")
        self.setFixedSize(1000, 750)
        
        self.processor = SketchProcessor()
        self.current_frame = None
        self.captured_image = None
        self.latest_nc_path = None
        
        self.prompts_dict = config.load_prompts()
        self.default_pen = config.PEN_PRESETS["네임펜"] # 기본값 고정
        self.api_key = "AIzaSyAAepYJsbdwtrVseJe3pqf0hKfvRz_yk1w" # 여기에 실제 API 키 입력
        
        self.init_ui()
        self.start_camera()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # 상단 스타일 선택 영역
        style_layout = QHBoxLayout()
        style_layout.addWidget(QLabel("1. 스타일을 선택하세요:"))
        self.combo_style = QComboBox()
        
        # 일반 스타일 추가
        for name in self.prompts_dict.keys():
            self.combo_style.addItem(name, ("GEMINI", None))
            
        # 캐릭터 스타일 동적 추가
        self.char_prompts_dict = config.load_character_prompts()
        if os.path.exists(config.CHARACTERS_DIR):
            char_files = [f for f in os.listdir(config.CHARACTERS_DIR) 
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for f in char_files:
                display_name = f"🐾 {os.path.splitext(f)[0]}와 함께"
                # 첫 번째 캐릭터 프롬프트를 기본으로 사용
                char_prompt = list(self.char_prompts_dict.values())[0]
                self.combo_style.addItem(display_name, ("GEMINI_CHAR", f, char_prompt))

        self.combo_style.setFixedHeight(40)
        style_layout.addWidget(self.combo_style)
        main_layout.addLayout(style_layout)

        # 중앙 이미지 영역 (카메라 또는 결과)
        img_container = QHBoxLayout()
        
        # 왼쪽: 라이브 카메라 / 촬영된 원본
        self.lbl_main = QLabel("카메라 준비 중...")
        self.lbl_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_main.setFixedSize(440, 440)
        self.lbl_main.setStyleSheet("border: 2px solid #ccc; background-color: black;")
        img_container.addWidget(self.lbl_main)

        # 화살표 아이콘 (또는 텍스트)
        arrow_lbl = QLabel("▶")
        arrow_lbl.setStyleSheet("font-size: 30px; color: #666;")
        img_container.addWidget(arrow_lbl)

        # 오른쪽: 최종 스케치 결과 프리뷰
        self.lbl_result = QLabel("결과가 여기에 표시됩니다")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setFixedSize(440, 440)
        self.lbl_result.setStyleSheet("border: 2px solid #4CAF50; background-color: #f9f9f9;")
        img_container.addWidget(self.lbl_result)
        
        main_layout.addLayout(img_container)

        # 하단 버튼 제어 영역
        btn_layout = QHBoxLayout()
        
        self.btn_capture = QPushButton("2. 사진 촬영")
        self.btn_capture.setFixedHeight(60)
        self.btn_capture.setStyleSheet("background-color: #2196F3; color: white; font-size: 18px; font-weight: bold;")
        self.btn_capture.clicked.connect(self.capture_image)
        btn_layout.addWidget(self.btn_capture)

        self.btn_retake = QPushButton("다시 찍기")
        self.btn_retake.setFixedHeight(60)
        self.btn_retake.setEnabled(False)
        self.btn_retake.clicked.connect(self.retake_photo)
        btn_layout.addWidget(self.btn_retake)

        self.btn_process = QPushButton("3. 로봇 그리기 시작")
        self.btn_process.setFixedHeight(60)
        self.btn_process.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; font-weight: bold;")
        self.btn_process.setEnabled(False)
        self.btn_process.clicked.connect(self.start_processing)
        btn_layout.addWidget(self.btn_process)

        main_layout.addLayout(btn_layout)

        # 진행바 및 상태 메시지
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)

        self.status_label = QLabel("준비 완료 - 스타일을 고르고 사진을 찍어주세요.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 14px; color: #333;")
        main_layout.addWidget(self.status_label)

    def start_camera(self):
        self.camera_thread = CameraThread(source=0)
        self.camera_thread.change_pixmap_signal.connect(self.update_camera_feed)
        self.camera_thread.start()

    def update_camera_feed(self, frame):
        if self.captured_image is None:
            self.current_frame = frame
            self.display_image(self.lbl_main, frame)

    def display_image(self, label, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
        pixmap = QPixmap.fromImage(qt_image)
        label.setPixmap(pixmap.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def capture_image(self):
        if self.current_frame is not None:
            self.captured_image = self.current_frame.copy()
            self.display_image(self.lbl_main, self.captured_image)
            self.btn_capture.setEnabled(False)
            self.btn_retake.setEnabled(True)
            self.btn_process.setEnabled(True)
            self.status_label.setText("사진이 촬영되었습니다. '로봇 그리기 시작'을 눌러주세요.")

    def retake_photo(self):
        self.captured_image = None
        self.btn_capture.setEnabled(True)
        self.btn_retake.setEnabled(False)
        self.btn_process.setEnabled(False)
        self.lbl_result.clear()
        self.lbl_result.setText("결과가 여기에 표시됩니다")
        self.status_label.setText("다시 촬영 준비됨.")

    def start_processing(self):
        if self.captured_image is None: return
        
        if not self.api_key:
            QMessageBox.critical(self, "오류", "Gemini API Key가 설정되지 않았습니다. (환경변수 확인)")
            return

        # 선택된 데이터 정보 가져오기
        data = self.combo_style.currentData()
        sketch_type, info = data[0], data[1:]
        
        character_image = None
        if sketch_type == "GEMINI":
            style_text = self.combo_style.currentText()
            prompt = self.prompts_dict[style_text]
        else: # GEMINI_CHAR
            char_filename, prompt = info[0], info[1]
            char_path = os.path.join(config.CHARACTERS_DIR, char_filename)
            img_array = np.fromfile(char_path, np.uint8)
            character_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        self.btn_process.setEnabled(False)
        self.btn_retake.setEnabled(False)
        self.status_label.setText("AI가 그림을 그리고 있습니다... 잠시만 기다려주세요.")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)

        self.worker = WorkerThread(
            self.processor, self.captured_image, sketch_type,
            gemini_api_key=self.api_key, gemini_prompt=prompt, 
            character_image=character_image, pen_config=self.default_pen,
            temperature=0.0
        )
        self.worker.progress_signal.connect(self.on_worker_progress)
        self.worker.finished_signal.connect(self.on_worker_finished)
        self.worker.error_signal.connect(self.handle_worker_error)
        self.worker.start()

    def on_worker_progress(self, step_id, image, message):
        self.status_label.setText(message)
        if image.size > 0 and (step_id == "sketch" or step_id == "done"):
            self.display_image(self.lbl_result, image)

    def handle_worker_error(self, error_msg):
        self.btn_process.setEnabled(True)
        self.btn_retake.setEnabled(True)
        self.progress_bar.setVisible(False)
        QMessageBox.critical(self, "처리 오류", error_msg)

    def on_worker_finished(self, results):
        self.progress_bar.setVisible(False)
        if results:
            nc_path = results[0]
            self.status_label.setText("로봇이 그리기를 시작합니다!")
            self.run_robot_drawing(nc_path)
        else:
            self.btn_process.setEnabled(True)
            self.btn_retake.setEnabled(True)
            QMessageBox.critical(self, "오류", "이미지 처리 실패.")

    def run_robot_drawing(self, nc_path):
        import subprocess
        robot_script = os.path.join(os.path.dirname(__file__), "modules", "fianl_drawing_robot.py")
        try:
            subprocess.Popen([sys.executable, robot_script, nc_path, "pen"])
            QMessageBox.information(self, "완료", "로봇이 드로잉을 시작했습니다!")
        except Exception as e:
            QMessageBox.warning(self, "실패", f"로봇 실행 실패: {e}")
        
        # 완료 후 초기화 준비
        self.btn_retake.setEnabled(True)

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = BasicUserGui()
    gui.show()
    sys.exit(app.exec())
