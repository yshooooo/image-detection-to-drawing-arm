import importlib
import importlib.util
import math
import os
import re
import sys
import time

import rclpy
from rclpy.logging import get_logger

ROBOT_ID = "dsr01"
ROBOT_MODEL = "a0509"

import DR_init

DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL

logger = get_logger("single_robot_simple_logger")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PY = os.path.join(BASE_DIR, "output_linear.py")
Y_Z_TOTAL_OFFSET = -0.6
Y_INTERPOLATION_LENGTH = 100.0
TARGET_DRAW_WIDTH_MM = 100.0
TARGET_DRAW_HEIGHT_MM = 100.0
SELECTED_PEN = "pen"

PEN_TCP_MAP = {
    "pen": "pen",
    "ball": "pen",
    "ballpen": "pen",
    "볼펜": "pen",
    "name": "name",
    "namepen": "name",
    "네임펜": "name",
    "maka": "maka",
    "marker": "maka",
    "마카": "maka",
}

PEN_PICK_CONFIG = {
    "pen": {
        "pick_pos": (89.10, 3.55, -76.70, -13.07, -89.77, 77.07),
        "pick_pose_down": (-91.69, -398.49, 366.76, 168.17, -177.60, 172.04),
        "pick_pose_up": (-91.69, -398.49, 566.76, 168.17, -177.60, 172.04),
    },
    "name": {
        "pick_pos": (89.10, 3.55, -76.70, -13.07, -89.77, 77.07),
        "pick_pose_down": (-27.64, -397.54, 361.28, 48.82, -178.55, 49.67),
        "pick_pose_up": (-27.64, -397.54, 461.28, 48.82, -178.55, 49.67),
    },
    "maka": {
        "pick_pos": (89.10, 3.55, -76.70, -13.07, -89.77, 77.07),
        "pick_pose_down": (22.64, -397.54, 361.28, 48.82, -178.55, 49.67),
        "pick_pose_up": (22.64, -397.54, 461.28, 48.82, -178.55, 49.67),
    },
}


def compress_path(points, tolerance=1e-4):
    if len(points) < 3:
        return points

    compressed = [points[0]]

    for i in range(1, len(points) - 1):
        x1, y1, _ = compressed[-1]
        x2, y2, _ = points[i]
        x3, y3, _ = points[i + 1]

        v1 = (x2 - x1, y2 - y1)
        v2 = (x3 - x2, y3 - y2)

        len1 = math.hypot(*v1)
        len2 = math.hypot(*v2)

        if len1 == 0 or len2 == 0:
            continue

        v1 = (v1[0] / len1, v1[1] / len1)
        v2 = (v2[0] / len2, v2[1] / len2)
        diff = math.hypot(v1[0] - v2[0], v1[1] - v2[1])

        if diff > tolerance:
            compressed.append(points[i])

    compressed.append(points[-1])
    return compressed


def gcode_to_dsr_function(input_nc, output_py):
    current_x = 0.0
    current_y = 0.0
    current_z = 0.0
    points = []

    with open(input_nc, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for raw_line in lines:
        line = raw_line.strip()

        if not (line.startswith("G0") or line.startswith("G1")):
            continue

        x_match = re.search(r"X([-+]?\d*\.?\d+)", line)
        y_match = re.search(r"Y([-+]?\d*\.?\d+)", line)
        z_match = re.search(r"Z([-+]?\d*\.?\d+)", line)

        if x_match:
            current_x = float(x_match.group(1))
        if y_match:
            current_y = float(y_match.group(1))
        if z_match:
            current_z = float(z_match.group(1))

        points.append((current_x / 3, current_y / 3, current_z))

    print(f"원래 점 개수: {len(points)}")
    points = compress_path(points)
    print(f"압축 후 점 개수: {len(points)}")

    if not points:
        raise ValueError("G-code에서 유효한 좌표를 찾지 못했습니다.")

    # 입력 G-code bbox를 고정 물리 크기(mm) 박스로 정규화
    xs = [x for x, _, _ in points]
    ys = [y for _, y, _ in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max_x - min_x
    span_y = max_y - min_y
    if span_x <= 1e-9 or span_y <= 1e-9:
        raise ValueError("G-code 경로 크기가 너무 작아 정규화할 수 없습니다.")
    mm_scale = min(TARGET_DRAW_WIDTH_MM / span_x, TARGET_DRAW_HEIGHT_MM / span_y)
    points = [
        ((x - min_x) * mm_scale, (y - min_y) * mm_scale, z)
        for x, y, z in points
    ]

    y_values = [y for _, y, _ in points]
    y_start = max(y_values)

    output = []
    output.append("from DSR_ROBOT2 import movel, posx\n\n")
    output.append(f"Y_START = {y_start:.6f}\n")
    output.append(f"Y_Z_TOTAL_OFFSET = {Y_Z_TOTAL_OFFSET:.6f}\n")
    output.append(f"Y_INTERPOLATION_LENGTH = {Y_INTERPOLATION_LENGTH:.6f}\n\n")
    output.append("def calc_z_offset(dy):\n")
    output.append("    if Y_INTERPOLATION_LENGTH <= 0:\n")
    output.append("        return 0.0\n")
    output.append("    ratio = (Y_START - dy) / Y_INTERPOLATION_LENGTH\n")
    output.append("    ratio = max(0.0, min(1.0, ratio))\n")
    output.append("    return Y_Z_TOTAL_OFFSET * ratio\n\n")
    output.append("def draw(cx, cy, cz):\n")
    output.append("    PEN_RPY = (0.0, 180.0, 90.0)\n")
    output.append("    vel = 80\n")
    output.append("    acc = 80\n\n")

    for x, y, z in points:
        output.append(f"    dx = {x:.3f}\n")
        output.append(f"    dy = {y:.3f}\n")
        output.append(f"    base_z = {z:.3f}\n")
        output.append(
            "    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), "
            "*PEN_RPY), vel=vel, acc=acc, r=1)\n\n"
        )

    with open(output_py, "w", encoding="utf-8") as file:
        file.writelines(output)

    print("Y 범위 기반 선형 Z 보정 output_linear.py 생성 완료!")


def main(args=None):
    input_nc_path = None
    selected_pen_name = SELECTED_PEN
    if args and len(args) > 0:
        input_nc_path = args[0]
    elif len(sys.argv) > 1:
        input_nc_path = sys.argv[1]
    if args and len(args) > 1:
        selected_pen_name = args[1]
    elif len(sys.argv) > 2:
        selected_pen_name = sys.argv[2]

    if not input_nc_path:
        raise ValueError(
            "G-code 파일 경로가 필요합니다. "
            "사용법: python fianl_drawing_robot.py <path_to_nc> [pen_name]"
        )

    print(f"사용 G-code 파일: {input_nc_path}")
    print(f"선택 펜: {selected_pen_name}")

    rclpy.init(args=[] if args is None else args)
    node = rclpy.create_node("single_robot_simple_py", namespace=ROBOT_ID)
    DR_init.__dsr__node = node

    time.sleep(2)

    try:
        from DSR_ROBOT2 import (
            ROBOT_MODE_AUTONOMOUS,
            get_current_posx,
            get_tcp,
            movej,
            movel,
            posj,
            posx,
            set_robot_mode,
            set_tcp,
            set_tool_digital_output,
        )
    except ImportError as exc:
        print(f"Error importing DSR_ROBOT2 : {exc}")
        return

    selected_key = selected_pen_name.strip().lower()
    selected_tcp = PEN_TCP_MAP.get(selected_key)
    if selected_tcp is None:
        valid_names = ", ".join(sorted(PEN_TCP_MAP.keys()))
        raise ValueError(
            f"지원하지 않는 펜 이름입니다: '{selected_pen_name}'. "
            f"가능한 값: {valid_names}"
        )
    selected_pick = PEN_PICK_CONFIG[selected_tcp]

    def open_gripper():
        print("그리퍼 열기 시도...")
        set_tool_digital_output(1, 1)
        time.sleep(1)
        set_tool_digital_output(1, 0)
        time.sleep(1)
        set_tool_digital_output(1, 1)
        time.sleep(1)
        set_tool_digital_output(1, 0)
        time.sleep(1)

    def close_gripper():
        print("그리퍼 닫기 시도...")
        set_tool_digital_output(2, 1)
        time.sleep(1)
        set_tool_digital_output(2, 0)
        time.sleep(1)

    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    p1 = posj(0, 0, 0, 0, 0, 0)

    camera_pos = posj(-90.19, -9.74, -132.50, -2.28, 54.36, 2.15) #joint

    pick_pos = posj(*selected_pick["pick_pos"])
    pick_pose_down = posx(*selected_pick["pick_pose_down"])
    pick_pose_up = posx(*selected_pick["pick_pose_up"])

    gcode_to_dsr_function(input_nc_path, OUTPUT_PY)

    print("\n=== 1. 펜 집기 작업 시작 ===")
    set_robot_mode(0)
    time.sleep(0.5)
    set_tcp("Tool_v1")
    time.sleep(0.5)
    set_robot_mode(1)
    time.sleep(0.5)

    movej(p1, vel=30, acc=30)
    open_gripper()
    movej(pick_pos, vel=30, acc=30)
    movel(pick_pose_up, vel=100, acc=100)
    movel(pick_pose_down, vel=100, acc=100)
    close_gripper()
    movel(pick_pose_up, vel=100, acc=100)

    print(f"\n=== 2. TCP 설정 ({selected_tcp}) ===")
    set_robot_mode(0)
    time.sleep(0.5)
    set_tcp(selected_tcp)
    time.sleep(0.5)
    set_robot_mode(1)
    time.sleep(0.5)
    current_tcp = get_tcp()
    logger.info(f"요청 TCP: {selected_tcp}, 현재 TCP: {current_tcp}")
    if current_tcp != selected_tcp:
        raise RuntimeError(
            f"TCP 변경 실패: requested='{selected_tcp}', current='{current_tcp}'. "
            "티칭펜던트 TCP 이름(대소문자/철자)을 확인하세요."
        )

    print("\n=== 3. 그림 그리기 작업 시작 ===")
    q_init = posj(-91.73, 4.21, -94.02, 1.68, -89.19, -1.72)
    movej(q_init, vel=20, acc=20)

    cur, _ = get_current_posx()
    cx, cy, cz, _, _, _ = cur

    lift = 20.0
    pen_rpy = (0.0, 180.0, 90.0)
    movel(posx(cx, cy, cz + lift, *pen_rpy), vel=50, acc=50)

    cz = -2
    movel(posx(cx, cy, cz, *pen_rpy), vel=50, acc=50)

    module_name = "output_linear"
    spec = importlib.util.spec_from_file_location(module_name, OUTPUT_PY)
    if spec is None or spec.loader is None:
        raise ImportError(f"생성된 모듈을 불러올 수 없습니다: {OUTPUT_PY}")
    output_linear = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = output_linear
    spec.loader.exec_module(output_linear)
    output_linear.draw(cx, cy, cz)

    movel(posx(cx, cy, cz + lift, *pen_rpy), vel=50, acc=50)

    set_robot_mode(0)
    time.sleep(0.5)
    set_tcp("Tool_v1")
    time.sleep(0.5)
    set_robot_mode(1)
    time.sleep(0.5)
    logger.info(f"현재 TCP: {get_tcp()}")

    movej(p1, vel=30, acc=30)

    movej(pick_pos, vel=30, acc=30)
    
    movel(pick_pose_up, vel=100, acc=100)
    movel(pick_pose_down, vel=100, acc=100)
    open_gripper()
    movel(pick_pose_up, vel=100, acc=100)
    movej(camera_pos, vel=30, acc=30)
    close_gripper()

    print("\n=== 모든 작업 완료! 수고하셨습니다. ===")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
