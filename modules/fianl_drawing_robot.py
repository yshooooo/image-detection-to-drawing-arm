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
NORMALIZE_TO_FIXED_BOX = False
RAW_COORD_SCALE = 1.0
TARGET_DRAW_WIDTH_MM = 100.0
TARGET_DRAW_HEIGHT_MM = 100.0
SELECTED_PEN = "pen"
BASE_TCP_NAME = "Tool_v1"
MIN_POINT_DISTANCE_MM = 0.5
RDP_EPSILON_MM = 0.3

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

# 펜 타입(내부 키) -> 티칭펜던트에 등록된 실제 TCP 이름
# 환경에 맞게 필요 시 값만 바꿔서 사용
DRAW_TCP_NAME_MAP = {
    "pen": "pen",
    "name": "name",
    "maka": "maka",
}

PEN_PICK_CONFIG = {
    "pen": {
        "pick_pos_a": (4.49, 43.69, -100.75, 25.60, -37.62, -23.92),
        "pick_pos_b": (85.61, -8.49, -60.60, 0.13, -110.91, 85.50),
        "pick_pose_down": (-81.69, -402.49, 366.76, 0, 180, 0),
        "pick_pose_up": (-81.69, -402.49, 566.76, 0, 180, 0),
    },
    "name": {
        "pick_pos_a": (4.49, 43.69, -100.75, 25.60, -37.62, -23.92),
        "pick_pos_b": (85.61, -8.49, -60.60, 0.13, -110.91, 85.50),
        "pick_pose_down": (-31.69, -402.49, 366.76, 0, 180, 0),
        "pick_pose_up": (-31.69, -402.49, 566.76, 0, 180, 0),
    },
    "maka": {
        "pick_pos_a": (4.49, 43.69, -100.75, 25.60, -37.62, -23.92),
        "pick_pos_b": (85.61, -8.49, -60.60, 0.13, -110.91, 85.50),
        "pick_pose_down": (17.69, -404.49, 366.76, 0, 180, 0) ,
        "pick_pose_up": (17.69, -404.49, 566.76, 0, 180, 0),
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


def point_distance_xy(point1, point2):
    return math.hypot(point2[0] - point1[0], point2[1] - point1[1])


def remove_close_points(points, min_dist=MIN_POINT_DISTANCE_MM):
    if len(points) < 3:
        return points[:]

    filtered = [points[0]]

    for point in points[1:-1]:
        if point_distance_xy(filtered[-1], point) >= min_dist:
            filtered.append(point)

    if filtered[-1] != points[-1]:
        filtered.append(points[-1])

    return filtered


def perpendicular_distance(point, start, end):
    x0, y0, _ = point
    x1, y1, _ = start
    x2, y2, _ = end

    dx = x2 - x1
    dy = y2 - y1
    line_length = math.hypot(dx, dy)

    if line_length <= 1e-9:
        return math.hypot(x0 - x1, y0 - y1)

    return abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / line_length


def rdp_simplify(points, epsilon=RDP_EPSILON_MM):
    if len(points) < 3:
        return points[:]

    start = points[0]
    end = points[-1]
    max_distance = -1.0
    split_index = -1

    for index in range(1, len(points) - 1):
        distance = perpendicular_distance(points[index], start, end)
        if distance > max_distance:
            max_distance = distance
            split_index = index

    if max_distance > epsilon:
        left = rdp_simplify(points[: split_index + 1], epsilon)
        right = rdp_simplify(points[split_index:], epsilon)
        return left[:-1] + right

    return [start, end]


def simplify_stroke(points):
    if len(points) < 3:
        return points[:]

    reduced_points = remove_close_points(points, MIN_POINT_DISTANCE_MM)
    return rdp_simplify(reduced_points, RDP_EPSILON_MM)


def build_motion_sequence(lines):
    current_x = 0.0
    current_y = 0.0
    current_z = 0.0
    motions = []
    stroke_points = []

    def flush_stroke():
        nonlocal stroke_points
        if not stroke_points:
            return

        for point in simplify_stroke(stroke_points):
            motions.append(("G1", point))

        stroke_points = []

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

        point = (current_x * RAW_COORD_SCALE, current_y * RAW_COORD_SCALE, current_z)

        if line.startswith("G0"):
            flush_stroke()
            motions.append(("G0", point))
        else:
            stroke_points.append(point)

    flush_stroke()
    return motions


def gcode_to_dsr_function(input_nc, output_py):
    with open(input_nc, "r", encoding="utf-8") as file:
        lines = file.readlines()

    current_x = 0.0
    current_y = 0.0
    current_z = 0.0
    raw_points = []

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

        raw_points.append((current_x * RAW_COORD_SCALE, current_y * RAW_COORD_SCALE, current_z))

    motions = build_motion_sequence(lines)
    points = [point for _, point in motions]

    print(f"원래 점 개수: {len(raw_points)}")
    print(f"압축 후 점 개수: {len(points)}")

    if not points:
        raise ValueError("G-code에서 유효한 좌표를 찾지 못했습니다.")

    xs = [x for x, _, _ in points]
    ys = [y for _, y, _ in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max_x - min_x
    span_y = max_y - min_y

    if NORMALIZE_TO_FIXED_BOX:
        # 필요할 때만 고정 물리 크기(mm) 박스로 정규화
        if span_x <= 1e-9 or span_y <= 1e-9:
            raise ValueError("G-code 경로 크기가 너무 작아 정규화할 수 없습니다.")
        mm_scale = min(TARGET_DRAW_WIDTH_MM / span_x, TARGET_DRAW_HEIGHT_MM / span_y)
        points = [
            ((x - min_x) * mm_scale, (y - min_y) * mm_scale, z)
            for x, y, z in points
        ]
        ys = [y for _, y, _ in points]
        min_y, max_y = min(ys), max(ys)
        span_y = max_y - min_y

    y_values = [y for _, y, _ in points]
    y_start = max(y_values)
    y_interp_len = span_y if span_y > 1e-9 else Y_INTERPOLATION_LENGTH

    output = []
    output.append("from DSR_ROBOT2 import movel, posx\n\n")
    output.append(f"Y_START = {y_start:.6f}\n")
    output.append(f"Y_Z_TOTAL_OFFSET = {Y_Z_TOTAL_OFFSET:.6f}\n")
    output.append(f"Y_INTERPOLATION_LENGTH = {y_interp_len:.6f}\n\n")
    output.append("def calc_z_offset(dy):\n")
    output.append("    if Y_INTERPOLATION_LENGTH <= 0:\n")
    output.append("        return 0.0\n")
    output.append("    ratio = (Y_START - dy) / Y_INTERPOLATION_LENGTH\n")
    output.append("    ratio = max(0.0, min(1.0, ratio))\n")
    output.append("    return Y_Z_TOTAL_OFFSET * ratio\n\n")
    output.append("def draw(cx, cy, cz):\n")
    output.append("    PEN_RPY = (0.0, 180.0, 90.0)\n")
    output.append("    vel = 100\n")
    output.append("    acc = 100\n\n")

    for _, (x, y, z) in motions:
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
            movesj,
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
    requested_tcp_name = DRAW_TCP_NAME_MAP.get(selected_tcp, selected_tcp)

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

    def _normalize_tcp_name(name):
        return str(name).strip().lower()

    def set_tcp_with_verify(target_tcp, retries=2):
        for attempt in range(retries + 1):
            set_robot_mode(0)
            time.sleep(0.5)
            set_tcp(target_tcp)
            time.sleep(0.5)
            set_robot_mode(1)
            time.sleep(0.5)

            current_tcp = get_tcp()
            logger.info(
                f"TCP 요청='{target_tcp}', 현재='{current_tcp}', 시도={attempt + 1}/{retries + 1}"
            )
            if _normalize_tcp_name(current_tcp) == _normalize_tcp_name(target_tcp):
                return current_tcp
        raise RuntimeError(
            f"TCP 변경 실패: requested='{target_tcp}', current='{current_tcp}'. "
            "티칭펜던트 TCP 이름(대소문자/철자)을 확인하세요."
        )

    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    p1 = posj(0, 0, 0, 0, 0, 0)

    camera_pos = posj(-90.19, -9.74, -132.50, -2.28, 54.36, 2.15) #joint

    pick_pos_a = posj(*selected_pick["pick_pos_a"])
    pick_pos_b = posj(*selected_pick["pick_pos_b"])
    pick_pose_down = posx(*selected_pick["pick_pose_down"])
    pick_pose_up = posx(*selected_pick["pick_pose_up"])

    gcode_to_dsr_function(input_nc_path, OUTPUT_PY)

    print("\n=== 1. 펜 집기 작업 시작 ===")
    set_tcp_with_verify(BASE_TCP_NAME)

    # movej(p1, vel=30, acc=30)
    open_gripper()
    movesj([pick_pos_a, pick_pos_b], vel=50, acc=50)
    movel(pick_pose_up, vel=100, acc=100)
    movel(pick_pose_down, vel=100, acc=100)
    close_gripper()
    movel(pick_pose_up, vel=100, acc=100)

    print(f"\n=== 2. TCP 설정 ({requested_tcp_name}) ===")
    set_tcp_with_verify(requested_tcp_name)

    print("\n=== 3. 그림 그리기 작업 시작 ===")
    q_init = posj(-91.73, 4.21, -94.02, 1.68, -89.19, -1.72)
    movej(q_init, vel=80, acc=80)

    # cur, _ = get_current_posx()
    cx, cy, cz = -50, 370, 300 

    lift = 20.0
    pen_rpy = (0.0, 180.0, 90.0)
    # movel(posx(cx, cy, cz + lift, *pen_rpy), vel=50, acc=50)

    cz = -24.5 # 볼펜
    # cz = -2.7 # 네임펜
    # cz = 4.5 # 마카

    # movel(posx(cx, cy, cz, *pen_rpy), vel=50, acc=50)

    module_name = "output_linear"
    spec = importlib.util.spec_from_file_location(module_name, OUTPUT_PY)
    if spec is None or spec.loader is None:
        raise ImportError(f"생성된 모듈을 불러올 수 없습니다: {OUTPUT_PY}")
    output_linear = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = output_linear
    spec.loader.exec_module(output_linear)
    output_linear.draw(cx, cy, cz)

    movel(posx(cx, cy, cz + lift, *pen_rpy), vel=50, acc=50)

    set_tcp_with_verify(BASE_TCP_NAME)
    logger.info(f"현재 TCP: {get_tcp()}")

    # movej(p1, vel=30, acc=30)

    movesj([pick_pos_a, pick_pos_b], vel=50, acc=50)
    
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
