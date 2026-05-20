import cv2
import os
import sys
import numpy as np
from modules import config, image_processor, generate_files_thinning

def main():
    """
    이미지를 입력받아 세선화(Thinning) 알고리즘을 적용하고, 
    G-Code(NC) 및 SVG 파일을 생성하는 스크립트입니다.
    기존의 image_processor와 thinning_converter 모듈을 활용합니다.
    """
    if len(sys.argv) < 2:
        print("사용법: python thinning_to_nc.py <입력_이미지_경로> [출력_nc_경로] [펜_이름] [--simple] [--no-bspline]")
        print("펜_이름: 네임펜, 볼펜, 마카 (기본값: 네임펜)")
        print("--simple: 배경 제거(rembg)를 건너뛰고 단순 이진화만 수행")
        print("--no-bspline: B-Spline 곡선 보간을 건너뛰고 원본 픽셀 경로 사용")
        print("예: python thinning_to_nc.py my_photo.jpg output.nc 볼펜 --simple --no-bspline")
        return

    input_path = sys.argv[1]
    
    # 인자 처리
    output_arg = None
    pen_name = "네임펜"
    use_simple = False
    use_bspline = True
    
    for arg in sys.argv[2:]:
        if arg == "--simple":
            use_simple = True
        elif arg == "--no-bspline":
            use_bspline = False
        elif arg in config.PEN_PRESETS:
            pen_name = arg
        elif not output_arg and not arg.startswith("--"):
            output_arg = arg

    if not os.path.exists(input_path):
        print(f"[오류] 파일을 찾을 수 없습니다: {input_path}")
        return

    # 펜 설정 적용
    if pen_name in config.PEN_PRESETS:
        preset = config.PEN_PRESETS[pen_name]
        config.Z_SAFE = preset.z_safe
        config.Z_DRAW = preset.z_draw
        config.FEED_RATE = preset.feed_rate
        print(f">> 펜 설정 적용: {pen_name} (Z_SAFE={config.Z_SAFE}, Z_DRAW={config.Z_DRAW})")
    else:
        print(f">> [경고] 알 수 없는 펜 이름 '{pen_name}'. 기본 설정을 사용합니다.")

    # 1. 이미지 로드
    img_array = np.fromfile(input_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if img is None:
        print(f"[오류] 이미지를 읽을 수 없습니다: {input_path}")
        return

    print(f">> 이미지 로드 완료: {input_path} ({img.shape[1]}x{img.shape[0]})")

    # 2. 전처리 (배경 제거 또는 단순 그레이스케일)
    if use_simple:
        print(">> [단계 1] 단순 그레이스케일 변환 및 블러 (배경 제거 건너뜀)...")
        processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed = cv2.GaussianBlur(processed, (5, 5), 0)
    else:
        print(">> [단계 1] 이미지 전처리 시작 (배경 제거 및 블러)...")
        processed = image_processor(img)
        
        if processed is None:
            print(">> [경고] image_processor 실패. 일반 그레이스케일 변환을 시도합니다.")
            processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            processed = cv2.GaussianBlur(processed, (5, 5), 0)

    # 3. 이진화 (Binary Thresholding)
    print(">> [단계 2] 이진화(Thresholding) 적용...")
    ret, binary = cv2.threshold(processed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    if ret < 100:
        _, binary = cv2.threshold(processed, 200, 255, cv2.THRESH_BINARY)
        print(f">> [정보] Otsu 임계값이 너무 낮아({ret}) 고정 임계값(200)을 사용합니다.")
    else:
        print(f">> [정보] Otsu 임계값 적용 완료: {ret}")
    
    # 중간 결과 확인을 위해 저장
    debug_dir = "debug"
    os.makedirs(debug_dir, exist_ok=True)
    binary_debug_path = os.path.join(debug_dir, "debug_binary.png")
    cv2.imwrite(binary_debug_path, binary)
    print(f">> 이진화 이미지 저장됨: {binary_debug_path}")

    # 4. 세선화 및 NC/SVG 파일 생성
    print(">> [단계 3] 세선화 및 G-Code 생성 시작...")
    
    if output_arg and output_arg.strip():
        nc_path = output_arg
    else:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        nc_path = os.path.join(output_dir, f"{base_name}_thinned.nc")
    
    svg_path = os.path.splitext(nc_path)[0] + ".svg"

    success = generate_files_thinning(binary, nc_path, svg_path, use_bspline=use_bspline)

    if success:
        print("=" * 50)
        print(f">> 작업 성공!")
        print(f">> NC 파일: {nc_path}")
        print(f">> SVG 파일: {svg_path}")
        print("=" * 50)
    else:
        print("[오류] 파일 생성에 실패했습니다.")

if __name__ == "__main__":
    main()
