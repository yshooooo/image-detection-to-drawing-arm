import sys
import os
import cv2
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QComboBox, QPushButton, 
                             QGroupBox, QFileDialog, QMessageBox, QScrollArea,
                             QLineEdit, QProgressBar)
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap

from modules import config
from modules.sketch_processor import SketchProcessor
from modules.human_cropper import detect_face_and_get_roi

class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self, source=0):
        super().__init__()
        self.source = source
        self._run_flag = True

    def run(self):
        # source가 'ZED'일 경우 ZED 라이브러리 연동이 필요할 수 있으나, 
        # 여기서는 일반 웹캠(0, 1...) 또는 파일 경로를 가정합니다.
        # ZED 사용 시 modules/camera_capture.py의 로직을 스레드화해야 함.
        cap = cv2.VideoCapture(self.source)
        while self._run_flag:
            ret, frame = cap.read()
            if ret:
                # 실시간 얼굴 감지 및 박스 그리기
                display_frame = frame.copy()
                try:
                    face_roi = detect_face_and_get_roi(frame)
                    if face_roi:
                        x1, y1, x2, y2 = face_roi
                        # 초록색 사각형 그리기 (BGR: (0, 255, 0), 두께: 2)
                        cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        # "ROI" 텍스트 추가
                        cv2.putText(display_frame, "ROI", (x1, y1 - 10), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                except Exception:
                    pass # 실시간 피드 중 오류 발생 시 무시 (성능 최우선)

                self.change_pixmap_signal.emit(display_frame)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class WorkerThread(QThread):
    progress_signal = pyqtSignal(str, np.ndarray, str)
    finished_signal = pyqtSignal(list)
    error_signal = pyqtSignal(str) # 에러 메시지 전용 시그널 추가

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
            import traceback
            error_msg = f"처리 중 오류가 발생했습니다:\n{str(e)}"
            # 인코딩 오류 등 상세 정보가 필요할 경우 traceback 포함 가능
            # error_msg += f"\n\n{traceback.format_exc()}"
            self.error_signal.emit(error_msg)

    def emit_progress(self, step_id, image, message):
        # 이미지가 None인 경우 빈 배열 전달
        img_to_send = image if image is not None else np.array([], dtype=np.uint8)
        self.progress_signal.emit(step_id, img_to_send, message)

class SketchGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 스케치 G-Code 변환기")
        self.resize(1200, 800)
        
        self.processor = SketchProcessor()
        self.current_frame = None
        self.captured_image = None # 초기화 명시
        self.character_image = None
        self.step_images = {} # 각 단계별 이미지 저장 (줌 시 재기록용)
        
        self.zoom_factor = 1.0 # 기본 줌 배율
        self.preview_labels = [] # 스케일링할 라벨 목록 추적
        
        self.prompts_dict = config.load_prompts()
        self.char_prompts_dict = config.load_character_prompts()
        
        self.init_ui()
        self.start_camera()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- 좌측 패널: 실시간 카메라 ---
        left_panel = QGroupBox("실시간 카메라")
        left_layout = QVBoxLayout()
        self.camera_label = QLabel("카메라 연결 중...")
        self.camera_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.camera_label.setFixedSize(400, 300)
        self.camera_label.setStyleSheet("background-color: black; color: white;")
        left_layout.addWidget(self.camera_label)
        
        self.btn_capture = QPushButton("사진 촬영")
        self.btn_capture.setFixedHeight(50)
        self.btn_capture.clicked.connect(self.capture_image)
        left_layout.addWidget(self.btn_capture)
        
        self.btn_load_file = QPushButton("파일에서 불러오기")
        self.btn_load_file.clicked.connect(self.load_image_file)
        left_layout.addWidget(self.btn_load_file)

        # --- 추가: 촬영/로드된 이미지를 보여줄 공간 ---
        left_layout.addSpacing(20)
        left_layout.addWidget(QLabel("선택된 이미지:"))
        self.captured_label = QLabel("이미지 없음")
        self.captured_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.captured_label.setFixedSize(400, 300)
        self.captured_label.setStyleSheet("border: 2px solid #4CAF50; background-color: #f9f9f9;")
        self.captured_label.setScaledContents(False)
        left_layout.addWidget(self.captured_label)
        
        left_layout.addStretch()
        left_panel.setLayout(left_layout)
        main_layout.addWidget(left_panel)

        # --- 중앙 패널: 변환 과정 Preview ---
        center_panel = QGroupBox("변환 과정 프리뷰")
        center_layout = QVBoxLayout()
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.preview_container = QWidget()
        self.preview_layout = QGridLayout(self.preview_container)
        self.preview_layout.setSpacing(10) # 사진 간 간격
        self.preview_layout.setContentsMargins(5, 5, 5, 5) # 테두리 여백 최소화
        self.preview_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft) # 상단 좌측 정렬 고정
        
        # 중앙 프리뷰 라벨 구성 변경 (2단계로 축소)
        self.lbl_step_cropped, w2 = self.create_preview_label("1. 객체/얼굴 추출")
        self.lbl_step_final, w4 = self.create_preview_label("2. 최종 스케치")
        
        # 중앙 패널에 2개의 과정 배치
        self.preview_layout.addWidget(w2, 0, 0)
        self.preview_layout.addWidget(w4, 0, 1)
        
        self.scroll_area.setWidget(self.preview_container)
        center_layout.addWidget(self.scroll_area)
        
        self.status_label = QLabel("준비 완료")
        self.status_label.setStyleSheet("font-weight: bold; color: blue;")
        center_layout.addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        center_layout.addWidget(self.progress_bar)

        center_panel.setLayout(center_layout)
        main_layout.addWidget(center_panel, 2) # 중앙 패널 비율 확장

        # --- 우측 패널: 사용자 컨트롤 ---
        right_panel = QGroupBox("사용자 컨트롤")
        right_layout = QVBoxLayout()

        # 입력 소스 (현재는 단순화)
        right_layout.addWidget(QLabel("입력 소스:"))
        self.combo_source = QComboBox()
        self.combo_source.addItems(["웹캠 (기본)", "ZED 카메라 (준비중)"])
        right_layout.addWidget(self.combo_source)

        # 스타일 선택
        right_layout.addWidget(QLabel("드로잉 스타일:"))
        self.combo_style = QComboBox()
        self.combo_style.addItems(list(self.prompts_dict.keys()))
        self.combo_style.addItem("캐릭터 동반 모드")
        self.combo_style.currentIndexChanged.connect(self.on_style_changed)
        right_layout.addWidget(self.combo_style)

        # 캐릭터 선택 (캐릭터 모드일 때만 활성화 예정)
        self.lbl_char = QLabel("합성 캐릭터:")
        right_layout.addWidget(self.lbl_char)
        self.combo_char = QComboBox()
        self.update_character_list()
        right_layout.addWidget(self.combo_char)

        # 캐릭터 동반 모드 상세 설정
        self.lbl_char_prompt = QLabel("캐릭터 동반 상세 설정:")
        right_layout.addWidget(self.lbl_char_prompt)
        self.combo_char_prompt = QComboBox()
        self.combo_char_prompt.addItems(list(self.char_prompts_dict.keys()))
        right_layout.addWidget(self.combo_char_prompt)

        # 펜 종류
        right_layout.addWidget(QLabel("펜 종류:"))
        self.combo_pen = QComboBox()
        for name in config.PEN_PRESETS.keys():
            self.combo_pen.addItem(name)
        right_layout.addWidget(self.combo_pen)

        # API Key (환경변수 없을 경우 입력)
        right_layout.addWidget(QLabel("Gemini API Key:"))
        self.edit_api_key = QLineEdit()
        self.edit_api_key.setEchoMode(QLineEdit.EchoMode.Password)
        if os.getenv("GEMINI_API_KEY"):
            self.edit_api_key.setText(os.getenv("GEMINI_API_KEY"))
            self.edit_api_key.setPlaceholderText("환경변수에서 로드됨")
        right_layout.addWidget(self.edit_api_key)

        right_layout.addStretch()

        self.btn_process = QPushButton("변환 및 G-Code 생성 시작")
        self.btn_process.setFixedHeight(60)
        self.btn_process.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; font-weight: bold;")
        self.btn_process.clicked.connect(self.start_processing)
        right_layout.addWidget(self.btn_process)

        right_panel.setLayout(right_layout)
        main_layout.addWidget(right_panel)

        # 초기 상태 설정
        self.on_style_changed()

    def create_preview_label(self, title):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0) # 전체 여백 제거
        layout.setSpacing(0) # 텍스트와 이미지 사이 간격 0으로 설정
        
        lbl_title = QLabel(title)
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # CSS를 통해 라벨 자체의 마진과 패딩을 0으로 강제
        lbl_title.setStyleSheet("font-weight: bold; font-size: 12px; margin: 0px; padding: 0px;")
        layout.addWidget(lbl_title)
        
        lbl_img = QLabel("이미지 없음")
        lbl_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # A4 비율(210:297 ≈ 1:1.414) 적용. 가로 300px 기준 세로 424px
        lbl_img.setFixedSize(300, 424)
        lbl_img.setStyleSheet("border: 1px solid #ccc; background-color: #f0f0f0; margin: 0px;")
        lbl_img.setScaledContents(False)
        self.preview_labels.append(lbl_img) # 줌 관리를 위해 목록에 추가
        layout.addWidget(lbl_img)
        return lbl_img, container

    def update_character_list(self):
        self.combo_char.clear()
        if os.path.exists(config.CHARACTERS_DIR):
            files = [f for f in os.listdir(config.CHARACTERS_DIR) 
                     if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            self.combo_char.addItems(files)
        if self.combo_char.count() == 0:
            self.combo_char.addItem("캐릭터 없음")

    def on_style_changed(self):
        is_char_mode = self.combo_style.currentText() == "캐릭터 동반 모드"
        self.combo_char.setEnabled(is_char_mode)
        self.lbl_char.setEnabled(is_char_mode)
        self.combo_char_prompt.setEnabled(is_char_mode)
        self.lbl_char_prompt.setEnabled(is_char_mode)

    def start_camera(self):
        self.camera_thread = CameraThread()
        self.camera_thread.change_pixmap_signal.connect(self.update_camera_feed)
        self.camera_thread.start()

    def update_camera_feed(self, frame):
        self.current_frame = frame
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
        pixmap = QPixmap.fromImage(qt_image)
        self.camera_label.setPixmap(pixmap.scaled(self.camera_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def capture_image(self):
        if self.current_frame is not None:
            self.captured_image = self.current_frame.copy()
            # 실시간 카메라는 그대로 두고, 아래 별도 라벨(captured_label)에 촬영된 사진 표시
            rgb_image = cv2.cvtColor(self.captured_image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
            self.captured_label.setPixmap(QPixmap.fromImage(qt_image).scaled(self.captured_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            
            self.status_label.setText("사진 촬영 완료. 설정을 확인 후 시작 버튼을 누르세요.")
            
            # 자동 프리뷰: 객체/얼굴 추출 단계 미리 채우기
            try:
                face_roi = detect_face_and_get_roi(self.captured_image)
                if face_roi:
                    x1, y1, x2, y2 = face_roi
                    cropped = self.captured_image[y1:y2, x1:x2]
                    self.display_preview(self.lbl_step_cropped, cropped)
                else:
                    self.lbl_step_cropped.setText("얼굴을 찾을 수 없음")
            except Exception:
                self.lbl_step_cropped.setText("추출 실패")

            # 촬영 시 다른 단계 초기화
            self.lbl_step_final.setText("준비 중...")

    def load_image_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 선택", config.GENERAL_INPUT_DIR, "Images (*.png *.jpg *.jpeg)")
        if file_path:
            img_array = np.fromfile(file_path, np.uint8)
            self.captured_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if self.captured_image is not None:
                # 로드된 사진을 아래 별도 라벨(captured_label)에 표시
                rgb_image = cv2.cvtColor(self.captured_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
                self.captured_label.setPixmap(QPixmap.fromImage(qt_image).scaled(self.captured_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                
                self.status_label.setText(f"파일 로드 완료: {os.path.basename(file_path)}")

                # 자동 프리뷰: 객체/얼굴 추출 단계 미리 채우기
                try:
                    face_roi = detect_face_and_get_roi(self.captured_image)
                    if face_roi:
                        x1, y1, x2, y2 = face_roi
                        cropped = self.captured_image[y1:y2, x1:x2]
                        self.display_preview(self.lbl_step_cropped, cropped)
                    else:
                        self.lbl_step_cropped.setText("얼굴을 찾을 수 없음")
                except Exception:
                    self.lbl_step_cropped.setText("추출 실패")
                
                # 로드 시 다른 단계 초기화
                self.lbl_step_final.setText("준비 중...")

    def display_preview(self, label, frame):
        if frame is None or frame.size == 0:
            return
        
        # 줌 시 재기록을 위해 이미지 저장
        self.step_images[label] = frame.copy()
        
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
        pixmap = QPixmap.fromImage(qt_image)
        # 비율을 유지하며 라벨 크기에 맞춰 스케일링 (왜곡 방지)
        label.setPixmap(pixmap.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def start_processing(self):
        if not hasattr(self, 'captured_image') or self.captured_image is None:
            QMessageBox.warning(self, "경고", "먼저 사진을 촬영하거나 파일을 불러와야 합니다.")
            return

        # 프리뷰 및 이미지 캐시 초기화
        self.step_images = {}
        for lbl in self.preview_labels:
            lbl.clear()
            lbl.setText("준비 중...")

        # 객체/얼굴 추출 다시 수행 및 표시
        try:
            face_roi = detect_face_and_get_roi(self.captured_image)
            if face_roi:
                x1, y1, x2, y2 = face_roi
                cropped = self.captured_image[y1:y2, x1:x2]
                self.display_preview(self.lbl_step_cropped, cropped)
            else:
                self.lbl_step_cropped.setText("얼굴을 찾을 수 없음")
        except Exception:
            self.lbl_step_cropped.setText("추출 실패")

        # 설정값 수집
        style_text = self.combo_style.currentText()
        pen_name = self.combo_pen.currentText()
        pen_config = config.PEN_PRESETS[pen_name]
        api_key = self.edit_api_key.text()
        
        if style_text == "캐릭터 동반 모드":
            sketch_type = 'GEMINI_CHAR'
            # 선택된 상세 프롬프트 사용
            selected_char_style = self.combo_char_prompt.currentText()
            prompt = self.char_prompts_dict.get(selected_char_style, list(self.char_prompts_dict.values())[0])
            char_file = self.combo_char.currentText()
            if char_file == "캐릭터 없음":
                self.character_image = None
            else:
                char_path = os.path.join(config.CHARACTERS_DIR, char_file)
                img_array = np.fromfile(char_path, np.uint8)
                self.character_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        else:
            sketch_type = 'GEMINI'
            prompt = self.prompts_dict[style_text]
            self.character_image = None

        # UI 상태 업데이트
        self.btn_process.setEnabled(False)
        self.status_label.setText("이미지 처리 중... 잠시만 기다려주세요.")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0) # 무한 루프 상태

        # 워커 스레드 시작
        self.worker = WorkerThread(
            self.processor, self.captured_image, sketch_type, 
            gemini_api_key=api_key, gemini_prompt=prompt, 
            character_image=self.character_image, pen_config=pen_config
        )
        self.worker.progress_signal.connect(self.on_worker_progress)
        self.worker.finished_signal.connect(self.on_worker_finished)
        self.worker.error_signal.connect(self.handle_worker_error) # 에러 시그널 연결
        self.worker.start()

    def on_worker_progress(self, step_id, image, message):
        self.status_label.setText(message)
        if image.size > 0:
            if step_id == "cropped" or step_id == "face_cropped":
                self.display_preview(self.lbl_step_cropped, image)
            elif step_id == "sketch" or step_id == "done":
                self.display_preview(self.lbl_step_final, image)

    def handle_worker_error(self, error_msg):
        self.btn_process.setEnabled(True)
        self.progress_bar.setVisible(False)
        QMessageBox.critical(self, "처리 오류", error_msg)
        self.status_label.setText("작업 실패.")

    def on_worker_finished(self, results):
        self.btn_process.setEnabled(True)
        self.progress_bar.setVisible(False)
        if results:
            QMessageBox.information(self, "완료", f"처리가 완료되었습니다.\n저장 경로: {results[0]}")
            self.status_label.setText("모든 작업 완료.")
        else:
            QMessageBox.critical(self, "오류", "이미지 처리 중 오류가 발생했습니다.")
            self.status_label.setText("작업 실패.")

    def wheelEvent(self, event):
        # Ctrl 키가 눌린 상태에서 휠을 돌릴 때만 줌 작동
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_factor *= 1.1 # 10% 확대
            else:
                self.zoom_factor *= 0.9 # 10% 축소
            
            # 줌 범위 제한 (0.5배 ~ 3.0배)
            self.zoom_factor = max(0.5, min(self.zoom_factor, 3.0))
            self.update_ui_scale()
            event.accept()
        else:
            super().wheelEvent(event)

    def update_ui_scale(self):
        # 기본 사이즈 정의
        base_w, base_h = 300, 424
        new_w = int(base_w * self.zoom_factor)
        new_h = int(base_h * self.zoom_factor)
        
        # 1. 프리뷰 라벨들 크기 조정
        for lbl in self.preview_labels:
            lbl.setFixedSize(new_w, new_h)
            
        # 2. 좌측 카메라 및 선택 이미지 라벨 크기 조정
        cam_w = int(400 * self.zoom_factor)
        cam_h = int(300 * self.zoom_factor)
        self.camera_label.setFixedSize(cam_w, cam_h)
        self.captured_label.setFixedSize(cam_w, cam_h)
        
        # 3. 저장된 모든 이미지들 다시 그리기 (줌 배율에 맞춰 리스케일링)
        for lbl, img in self.step_images.items():
            # display_preview를 직접 호출하면 step_images에 중복 저장되므로 로직 분리하거나 
            # 단순히 여기서 리스케일링만 수행
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).copy()
            pixmap = QPixmap.fromImage(qt_image)
            lbl.setPixmap(pixmap.scaled(lbl.width(), lbl.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        if hasattr(self, 'captured_image') and self.captured_image is not None:
            self.display_preview(self.captured_label, self.captured_image)
            
        self.status_label.setText(f"화면 배율: {int(self.zoom_factor * 100)}%")

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SketchGui()
    gui.show()
    sys.exit(app.exec())
