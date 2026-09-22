# Image Detection to Drawing Arm

사람의 사진을 AI로 선화 및 캐리커처로 변환하고, ROS2 기반 협동로봇이 생성된 그림을 캔버스에 직접 그려주는 시스템입니다.

## 프로젝트 개요

* **목표**: 사람의 안면 사진을 입력받아 AI로 선화 이미지를 생성하고, 협동로봇이 펜을 직접 집어 캔버스에 그림을 그리는 체험형 시스템 구현
* **주요 기능**: 카메라 촬영 -> 인물 인식 및 크롭 -> AI 스케치 변환 -> 세선화(thinning) 및 G-code 변환 -> 로봇 드로잉
* **사용 장비**: 두산로보틱스 협동로봇(A0509), 엔드이펙터/그리퍼(JEGH-3520P)
* **개발 환경**: Ubuntu 22.04 LTS, ROS2 Humble
* **주요 기술 스택**: Python, PyQt6, OpenCV, MediaPipe, Google Gemini API, ROS2, DSR_ROBOT2 Python API
* **기간**: 2025.09.02 ~ 2026.06.15 (원본 팀 프로젝트 기준, 이후 개인 확장 작업 진행)

## 갤러리

<img width="214" height="317" alt="image" src="https://github.com/user-attachments/assets/15967f83-8e0a-4290-bd19-922a9e1b4df4" />
<img width="214" height="317" alt="KakaoTalk_20260915_120636676" src="https://github.com/user-attachments/assets/7f1598b0-0b4d-493d-af2c-e8125f814a39" />
<img width="388" height="280" alt="KakaoTalk_20260915_120636676_01" src="https://github.com/user-attachments/assets/57c80955-92df-4c47-9ec7-c1964ada5bef" />

## 상세 설명

### 문제 정의

* 기존 산업용 로봇은 정해진 공정을 반복하는 자동화 작업에 집중되어 있어, 사람의 사진이나 창작물을 직접 그리는 예술 및 전시 중심의 응용 사례는 상대적으로 드뭅니다.
* 비전문가도 카메라 앞에서 사진을 촬영하는 것만으로 자신의 캐리커처를 로봇이 직접 그려주는 직관적인 체험형 시스템을 구현하고자 했습니다.

### 해결 방안

* 사용자의 사진을 카메라로 촬영하고, 인물 영역을 자동으로 검출 및 크롭한 뒤 Gemini API를 이용해 선화 및 캐리커처를 생성합니다.
* 생성된 이미지를 이진화하고 세선화(skeletonization)하여 로봇이 추적할 수 있는 얇은 드로잉 경로로 변환하고 G-code(.nc)를 생성합니다.
* ROS2와 DSR_ROBOT2 Python API를 이용해 두산 협동로봇을 제어하고, 로봇이 직접 펜을 집은 뒤 TCP를 전환하여 생성된 경로를 따라 그림을 그립니다.
* 전시 및 체험 환경을 고려한 PyQt6 기반 키오스크 GUI를 제공하여 사용자가 펜, 스타일, 캐릭터 동작을 직접 선택하고 드로잉 과정을 진행할 수 있도록 구성했습니다.

## 주요 기능

* **이미지 입력 및 전처리**: OpenCV 기반 카메라 촬영, MediaPipe 기반 얼굴 및 인물 영역 검출, 자동 크롭 및 이미지 전처리
* **Gemini 초상화 모드**: Google Gemini API를 활용하여 여러 스타일의 라인아트 및 캐리커처 생성
* **캐릭터 동반 모드**: 사용자 인물 사진과 캐릭터 이미지를 함께 이용해 하나의 선화 이미지 생성
* **세선화 및 경로 변환**: 생성된 이미지를 이진화하고 세선화(thinning)한 뒤 B-Spline을 적용하여 드로잉 경로를 생성하고 G-code(.nc)와 SVG로 저장
* **로봇 드로잉 제어**: G-code 좌표를 로봇 작업 좌표계로 변환하고 펜 종류별 TCP 및 픽업 좌표를 설정하여 `movej`, `movel`, `movesj` 기반으로 펜 픽업 -> 드로잉 -> 펜 반납까지 자동화
* **드로잉 경로 최적화**: 근접 좌표 제거와 RDP 알고리즘을 적용하여 불필요한 이동 좌표를 줄이고 로봇 드로잉 경로를 단순화
* **서명 자동 그리기**: 별도의 서명용 G-code를 읽어 너무 짧은 stroke를 제거하고 크기와 위치를 조정하여 드로잉 이후 서명까지 자동 수행
* **키오스크 GUI**: PyQt6 기반으로 펜, 스타일, 캐릭터 동작을 선택할 수 있는 무인 체험형 화면 제공
* **교육 및 체험 활용**: 전시장 실시간 체험, 캐리커처 제작, 로봇 예술 및 로봇 제어 교육 등에 활용 가능

## 실행 방법

### 1. 프로젝트 다운로드

```bash
git clone https://github.com/yshooooo/image-detection-to-drawing-arm.git
cd image-detection-to-drawing-arm
```

### 2. Python 패키지 설치

```bash
pip install -r requirements.txt
pip install PyQt6
```

### 3. Gemini API Key 설정

프로젝트 루트 디렉터리에 `.env` 파일을 생성하고 Gemini API Key를 입력합니다.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Gemini 기반 초상화 및 캐릭터 동반 모드를 사용하기 위해 필요합니다.

### 4. ROS2 및 Doosan Robotics 환경 설정

로봇 제어 기능을 사용하려면 ROS2 Humble과 두산로보틱스의 `doosan-robot2` 패키지가 설치되어 있어야 합니다.

ROS2 환경을 불러옵니다.

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

실제 a0509 로봇을 사용하는 경우 별도의 터미널에서 두산로보틱스 ROS2 bringup을 실행합니다.

```bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py \
  mode:=real \
  host:=ROBOT_IP \
  port:=12345 \
  model:=a0509
```

`ROBOT_IP` 부분은 실제 두산로보틱스 컨트롤러의 IP 주소로 변경해야 합니다.

### 5. 키오스크 프로그램 실행

새 터미널에서 ROS2 환경을 다시 불러옵니다.

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
cd image-detection-to-drawing-arm
```

키오스크 GUI를 실행합니다.

```bash
python3 user_gui_kiosk.py
```

프로그램 실행 후 전체 과정은 다음과 같습니다.

```text
카메라 촬영
-> 펜 선택
-> AI 스케치 모드 및 스타일 선택
-> Gemini 선화 생성
-> 이진화 및 세선화
-> G-code 생성
-> 로봇 펜 픽업
-> 로봇 드로잉
-> 서명
-> 펜 반납
```

지원하는 주요 펜 타입은 다음과 같습니다.

```text
pen  : 볼펜
name : 네임펜
maka : 마카
```

## 로봇 실행 시 주의사항

`modules/fianl_drawing_robot.py`에 설정된 로봇 좌표와 TCP 값은 프로젝트에서 사용한 a0509 및 실제 작업 환경을 기준으로 작성되어 있습니다.

다른 로봇 또는 다른 작업 환경에서 실행할 경우 다음 설정을 먼저 확인해야 합니다.

* 로봇 모델 및 ROS2 Namespace
* 두산로보틱스 컨트롤러 IP
* 기본 TCP 이름
* 펜 종류별 TCP
* 펜 픽업 및 반납 위치
* 캔버스 위치
* 로봇 드로잉 기준 좌표
* 그리퍼 Digital I/O 설정

특히 `PEN_PICK_CONFIG`, `DRAW_TCP_NAME_MAP` 등의 값은 실제 로봇 및 작업 환경에 맞게 조정해야 합니다.

잘못된 좌표를 사용할 경우 로봇이 의도하지 않은 위치로 이동할 수 있으므로 실제 로봇을 구동하기 전에 반드시 좌표와 작업 영역을 확인해야 합니다.

## 프로젝트 기여자

* 윤성민 (Project Leader)
* 양성호 (Robot Manipulation)
* 정준호 (Robot Manipulation)
* 손지훈 (Image Detection)
* 기이루 (Image Detection)

## 참고 자료

* https://github.com/DoosanRobotics/doosan-robot2
* https://manual.doosanrobotics.com/ko/programming-manual/3.3.0/publish/
* https://github.com/gns1643/image-detection-to-drawing-arm (Ref.)
