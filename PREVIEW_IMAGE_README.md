# 프리뷰 이미지 파일명 규칙

`user_gui_kiosk.py`는 모드/스타일/캐릭터 선택 화면의 왼쪽 미리보기를 `data/preview` 폴더에서 읽습니다.

## 초상화 스타일 프리뷰

권장 파일명:

```text
data/preview/portrait_스타일명.png
```

현재 설정 기준:

```text
data/preview/portrait_준호스타일.png
data/preview/portrait_익살스럽게.png
```

기존 인덱스 방식도 지원합니다.

```text
data/preview/portrait_style_1.png
data/preview/portrait_style_2.png
```

## 캐릭터 모드 프리뷰

권장 파일명:

```text
data/preview/character_캐릭터파일명_action_동작명.png
```

캐릭터 파일명은 확장자를 제외하고, 공백은 `_`로 바꿉니다.

현재 설정 기준:

```text
data/preview/character_11-06_A_인사_action_1.png
data/preview/character_11-06_A_인사_action_2.png
data/preview/character_11-06_A_인사_action_3.png
data/preview/character_11-06_A_인사_action_4.png
```

## 추가 방법

1. 초상화 스타일은 `config/gemini_prompts.json`에 추가합니다.
2. 캐릭터 동작은 `config/gemini_character_prompts.json`에 추가합니다.
3. 캐릭터 이미지는 `data/characters`에 넣습니다.
4. 대응하는 프리뷰 이미지를 `data/preview`에 넣습니다.
5. `user_gui_kiosk.py`를 다시 실행합니다.

앱 실행 중에 파일을 추가해도 화면에는 즉시 반영되지 않습니다. 추가 후 다시 실행해야 합니다.
