# Image Detection to Drawing Arm

사람의 사진을 AI로 선화/캐리커처로 변환하고, ROS2 기반 협동로봇이 그 그림을 캔버스에 직접 그려주는 시스템

## 프로젝트 개요

* **목표**: 사람의 안면 사진을 입력받아 AI로 선화 이미지를 생성하고, 협동로봇이 펜을 직접 집어 캔버스에 그 그림을 그리는 체험형 시스템 구현
* **주요 기능**: 카메라 촬영 → 인물 인식/크롭 → AI 스케치 변환 → 세선화(thinning) 및 G-code 변환 → 로봇 드로잉
* **사용 장비**: 두산로보틱스 협동로봇(A0509), 엔드이펙터/그리퍼(JEGH-3520P)
* **개발 환경**: Ubuntu 22.04 LTS, ROS2 Humble
* **주요 기술 스택**: Python, PyQt6, OpenCV, MediaPipe, Google Gemini API, ROS2, DSR_ROBOT2 Python API
* **기간**: 2025.09.02 ~ 2026.06.15 (원본 팀 프로젝트 기준, 이후 개인 확장 작업 진행)

## 갤러리
<img width="214" height="317" alt="image" src="https://github.com/user-attachments/assets/15967f83-8e0a-4290-bd19-922a9e1b4df4" />
<img width="214" height="317" alt="KakaoTalk_20260915_120636676" src="https://github.com/user-attachments/assets/7f1598b0-0b4d-493d-af2c-e8125f814a39" />
<img width="388" height="280" alt="KakaoTalk_20260915_120636676_01" src="https://github.com/user-attachments/assets/57c80955-92df-4c47-9ec7-c1964ada5bef" />

## 상세 설명

### 문제정의

* 기존 산업용 로봇은 정해진 공정을 반복하는 자동화 작업에 집중되어 있어, 사람의 사진이나 창작물을 직접 그리는 예술/전시 중심의 응용 사례는 상대적으로 드묾
* 비전문가도 카메라 앞에 서기만 하면 자신의 캐리커처를 로봇이 그려주는 직관적이고 체험 가능한 시스템의 부재

### 해결방안

* 사용자의 사진을 카메라로 촬영하고, 인물 영역을 자동으로 검출/크롭한 뒤 Gemini API를 통해 선화/캐리커처를 생성
* 생성된 이미지를 이진화 → 세선화(skeletonization)하여 로봇이 추적할 수 있는 얇은 드로잉 경로로 변환하고, 이를 G-code(.nc)로 자동 생성
* ROS2와 DSR_ROBOT2 Python API를 활용해 두산 협동로봇을 제어하고, 펜을 직접 집은 뒤 TCP를 전환하여 생성된 경로를 따라 캔버스에 그림
* 전시/체험 환경을 고려한 PyQt6 기반 키오스크 GUI를 제공하여, 관리자 개입 없이 사용자가 펜과 스타일을 선택하고 드로잉 과정을 진행할 수 있도록 구성

### 주요기능

* **이미지 입력 및 전처리**: OpenCV 기반 카메라 촬영, MediaPipe 기반 얼굴 및 인물 영역 검출, 자동 크롭 및 이미지 전처리
* **AI 스케치 생성**

* **Gemini 초상화 모드**: Google Gemini API를 활용하여 여러 스타일의 라인아트/캐리커처 생성
* **캐릭터 동반 모드**: 사용자 인물 사진과 캐릭터 이미지를 함께 활용해 하나의 선화 이미지 생성
* **세선화 및 경로 변환**: 생성된 이미지를 이진화하고 세선화(thinning)한 뒤 B-Spline을 적용하여 드로잉 경로를 생성하고, G-code(.nc)와 SVG로 저장
* **로봇 드로잉 제어**: G-code 좌표를 로봇 작업 좌표계로 변환하고, 펜 종류별 TCP 및 픽업 좌표를 설정하여 movej, movel, movesj 기반으로 펜 픽업 → 드로잉 → 펜 반납까지 전 과정 자동화
* **드로잉 경로 최적화**: 근접 좌표 제거와 RDP 알고리즘을 적용하여 불필요한 이동 좌표를 줄이고 로봇 드로잉 경로를 단순화
* **서명(사인) 자동 그리기**: 별도의 사인용 G-code를 읽어 너무 짧은 stroke를 제거하고 크기와 위치를 조정하여 드로잉 이후 서명까지 자동 수행
* **키오스크 GUI**: PyQt6 기반으로 펜, 스타일, 캐릭터 동작을 선택할 수 있는 무인 체험형 화면 제공
* **교육/체험/예술 응용**: 전시장 실시간 체험, 캐리커처 제작, 로봇 예술 교육 도구 등으로 활용 가능

## 프로젝트 기여자

* 윤성민(Project Leader) 
* 양성호(Robot Manipulation) 
* 정준호(Robot Manipulation) 
* 손지훈(Image Detection) 
* 기이루(Image Detection) 

## 참고자료

* https://github.com/DoosanRobotics/doosan-robot2
* https://manual.doosanrobotics.com/ko/programming-manual/3.3.0/publish/
* https://github.com/gns1643/image-detection-to-drawing-arm (Ref.)
