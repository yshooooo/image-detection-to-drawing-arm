# Image Detection to Drawing Arm

사람의 사진을 AI로 선화/캐리커처로 변환하고, ROS2 기반 협동로봇이 그 그림을 캔버스에 직접 그려주는 시스템

## 프로젝트 개요

* **목표**: 사람의 안면 사진을 입력받아 AI로 선화 이미지를 생성하고, 협동로봇이 펜을 직접 집어 캔버스에 그 그림을 그리는 휴먼 인터페이스 기반 시스템 구현
* **주요 기능**: 웹캠 촬영 또는 이미지 파일 입력 → 인물 인식/크롭 → AI 스케치 변환 → 세선화(thinning) 및 G-code 변환 → 로봇 드로잉
* **사용 장비**: 두산로보틱스 협동로봇 (a0609), 엔드이펙터/그리퍼(JEGH-3520P)
* **개발 환경**: Ubuntu 22.04 LTS, ROS2 Humble
* **주요 기술 스택**: ROS2, OpenCV, MediaPipe, PyTorch, Google Gemini API, Tkinter
* **기간**: 2025.09.02 \~ 2026.06.15 (원본 팀 프로젝트 기준, 이후 개인 확장 작업 진행)

## 갤러리
<img width="214" height="317" alt="image" src="https://github.com/user-attachments/assets/15967f83-8e0a-4290-bd19-922a9e1b4df4" />
<img width="214" height="317" alt="KakaoTalk_20260915_120636676" src="https://github.com/user-attachments/assets/7f1598b0-0b4d-493d-af2c-e8125f814a39" />
<img width="388" height="280" alt="KakaoTalk_20260915_120636676_01" src="https://github.com/user-attachments/assets/57c80955-92df-4c47-9ec7-c1964ada5bef" />



## 상세 설명

### 문제정의

* 기존 산업용 로봇은 정해진 공정을 반복하는 자동화 작업에 집중되어 있어, 사람의 사진이나 창작물을 그대로 따라 그리는 예술/전시 중심 응용 사례는 드묾
* 비전문가도 카메라 앞에 서기만 하면 자신만의 캐리커처를 로봇이 그려주는, 직관적이고 체험 가능한 시스템의 부재

### 해결방안

* 사용자의 웹캠 촬영 또는 이미지 파일을 입력받아, 인물 영역을 자동으로 검출/크롭한 뒤 AI 모델로 선화/캐리커처를 생성
* 생성된 이미지를 이진화 → 세선화(skeletonization)하여 한 붓 그리기가 가능한 얇은 경로로 변환하고, 이를 로봇 좌표계에 맞는 G-code(.nc)로 자동 생성
* ROS2로 두산 협동로봇을 제어하여, 펜을 스스로 집고(TCP 자동 전환/그리퍼 디지털 출력 제어) 변환된 경로를 따라 캔버스에 직접 그림
* 전시/체험 환경을 고려한 Tkinter 기반 키오스크 GUI를 별도로 제공하여, 관리자 개입 없이도 사용자가 스타일과 캐릭터를 선택해 그림을 완성할 수 있도록 구성

### 주요기능

* **이미지 입력 및 전처리**: 웹캠 실시간 촬영 또는 로컬 이미지 불러오기, MediaPipe 기반 인물 검출 및 자동 크롭, 밝기/선명도 등 이미지 보정
* **AI 스케치 생성 (2가지 모드)**

* **로컬 AI 모드**: PyTorch 기반 모델로 애니메이션풍 선화 생성
* **Gemini 모드**: Google Gemini API로 고품질 라인아트/캐리커처 생성, 프롬프트는 JSON 설정 파일로 관리하며 여러 스타일을 한 번에 순차 생성하는 배치 모드 지원
* **캐릭터 동반 모드**: 사용자 인물 사진과 캐릭터 이미지를 함께 합성해 한 장면으로 그려주는 선화 생성
* **세선화 및 경로 변환**: Canny/이진화/세선화(thinning) 세 가지 방식으로 이미지를 얇은 선 경로로 변환, 결과를 G-code(.nc)와 SVG로 동시 저장
* **로봇 드로잉 제어**: G-code 좌표를 로봇 작업 좌표계로 변환, 펜 종류별 TCP 픽업 좌표 설정, movej/movel/movesj로 펜 픽업 → 드로잉 → 펜 리턴까지 전 과정 자동화
* **서명(사인) 자동 그리기**: 별도의 사인용 G-code를 읽어 너무 짧은 stroke를 제거/연결하고 크기/위치를 자동으로 스케일링해 안정적으로 그리는 기능
* **키오스크 GUI**: 스타일/캐릭터 동작을 썸네일 미리보기로 선택할 수 있는 무인 체험형 화면 제공, 설정 파일과 미리보기 이미지만 추가하면 스타일/캐릭터 구성을 손쉽게 확장 가능
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

