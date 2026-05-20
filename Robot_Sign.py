import importlib.util
import math
import os
import sys
import time

import rclpy
from rclpy.logging import get_logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HELPER_PATH = os.path.join(BASE_DIR, "modules", "fianl_drawing_robot.py")
SIGN_NC_PATH = os.path.join(BASE_DIR, "Robot_Sign.nc")
SIGN_OUTPUT_PY = os.path.join(BASE_DIR, "modules", "output_linear_sign.py")

# 사인 위치는 고정 좌표로 사용
SIGN_DRAW_CX = 0.0
SIGN_DRAW_CY = 240.0
SIGN_LIFT_MM = 20.0
SIGN_SCALE_FACTOR = 0.3
SIGN_Y_Z_TOTAL_OFFSET = -0.2
SIGN_Y_INTERPOLATION_LENGTH = 100.0
DEFAULT_PEN = "name"
DRAW_READY_JOINT = (-91.73, 4.21, -94.02, 1.68, -89.19, -1.72)
CAMERA_POS_JOINT = (-90.19, -9.74, -132.50, -2.28, 54.36, 2.15)
SIGN_MIN_STROKE_LENGTH_MM = 1.2
SIGN_BRIDGE_GAP_MM = 6.0


def load_module(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"모듈을 불러올 수 없습니다: {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


helper = load_module("sign_helper_module", HELPER_PATH)
logger = get_logger("robot_sign_logger")


def point_distance_xy(point1, point2):
    return math.hypot(point2[0] - point1[0], point2[1] - point1[1])


def stroke_length(points):
    return sum(point_distance_xy(start, end) for start, end in zip(points, points[1:]))


def remove_tiny_strokes(
    motions,
    min_stroke_length_mm=SIGN_MIN_STROKE_LENGTH_MM,
    bridge_gap_mm=SIGN_BRIDGE_GAP_MM,
):
    strokes = []
    current_stroke = []
    current_g0_point = None

    for command, point in motions:
        if command == "G0":
            if current_stroke:
                strokes.append((current_g0_point, current_stroke))
                current_stroke = []
            current_g0_point = point
            continue
        current_stroke.append(point)

    if current_stroke:
        strokes.append((current_g0_point, current_stroke))

    if not strokes:
        return []

    removed_count = 0
    bridged_count = 0
    bridged_removed_count = 0

    stroke_infos = [
        {
            "g0_point": g0_point,
            "points": stroke[:],
            "length": stroke_length(stroke),
        }
        for g0_point, stroke in strokes
    ]

    kept_strokes = []
    index = 0
    while index < len(stroke_infos):
        info = stroke_infos[index]
        if info["length"] >= min_stroke_length_mm:
            kept_strokes.append((info["g0_point"], info["points"][:]))
            index += 1
            continue

        removed_start = index
        while index < len(stroke_infos) and stroke_infos[index]["length"] < min_stroke_length_mm:
            index += 1

        removed_run_count = index - removed_start
        removed_count += removed_run_count

        prev_kept = kept_strokes[-1] if kept_strokes else None
        next_info = stroke_infos[index] if index < len(stroke_infos) else None
        if prev_kept is None or next_info is None:
            continue

        gap = point_distance_xy(prev_kept[1][-1], next_info["points"][0])
        if gap > bridge_gap_mm:
            continue

        if prev_kept[1][-1] != next_info["points"][0]:
            prev_kept[1].append(next_info["points"][0])
        prev_kept[1].extend(next_info["points"][1:])
        bridged_count += 1
        bridged_removed_count += removed_run_count
        index += 1

    if not kept_strokes:
        raise ValueError("사인 경로에서 너무 짧지 않은 스트로크를 찾지 못했습니다.")

    filtered_motions = []
    for g0_point, stroke in kept_strokes:
        if g0_point is not None:
            filtered_motions.append(("G0", g0_point))
        filtered_motions.extend(("G1", point) for point in stroke)

    before_lengths = [stroke_length(stroke) for _, stroke in strokes]
    after_lengths = [stroke_length(stroke) for _, stroke in kept_strokes]
    print(
        "사인 짧은 스트로크 제거:",
        f"{len(strokes)}개 -> {len(kept_strokes)}개,",
        f"제거 {removed_count}개,",
        f"브리지 {bridged_count}회({bridged_removed_count}개 구간),",
        f"임계값 {min_stroke_length_mm:.3f}mm/{bridge_gap_mm:.3f}mm",
    )

    return filtered_motions


def scale_sign_motions(motions, scale_factor=SIGN_SCALE_FACTOR):
    if not motions:
        return []

    if scale_factor <= 0:
        raise ValueError(f"사인 축소 비율은 0보다 커야 합니다: {scale_factor}")

    if math.isclose(scale_factor, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        return motions

    points = [point for _, point in motions]
    bounds = helper.get_points_bounds(points)
    anchor_x = bounds["center_x"]
    anchor_y = bounds["center_y"]

    scaled_motions = []
    for command, (x, y, z) in motions:
        scaled_x = anchor_x + (x - anchor_x) * scale_factor
        scaled_y = anchor_y + (y - anchor_y) * scale_factor
        scaled_motions.append((command, (scaled_x, scaled_y, z)))

    scaled_bounds = helper.get_points_bounds([point for _, point in scaled_motions])
    print(
        "사인 크기 조정:",
        f"scale={scale_factor:.3f},",
        f"X {bounds['span_x']:.3f}mm -> {scaled_bounds['span_x']:.3f}mm,",
        f"Y {bounds['span_y']:.3f}mm -> {scaled_bounds['span_y']:.3f}mm",
    )
    return scaled_motions


def generate_sign_output(input_nc_path, output_py_path):
    with open(input_nc_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 사인은 y가 낮아질수록 z를 더 높이는 보정 로직을 사용한다.
    helper.Y_Z_TOTAL_OFFSET = SIGN_Y_Z_TOTAL_OFFSET
    helper.Y_INTERPOLATION_LENGTH = SIGN_Y_INTERPOLATION_LENGTH

    raw_points = helper.read_gcode_points(input_nc_path, coord_scale=helper.RAW_COORD_SCALE)
    motions = helper.build_transformed_motions(lines, coord_scale=helper.RAW_COORD_SCALE)
    filtered_motions = remove_tiny_strokes(motions)
    scaled_motions = scale_sign_motions(filtered_motions)

    if not scaled_motions:
        raise ValueError("사인 G-code에서 유효한 경로를 찾지 못했습니다.")

    print(f"원래 점 개수: {len(raw_points)}")
    print(f"압축 후 점 개수: {len([point for _, point in motions])}")
    print(f"제거 후 점 개수: {len([point for _, point in filtered_motions])}")
    print(f"크기 조정 후 점 개수: {len([point for _, point in scaled_motions])}")
    print(
        "사인 Y-Z 보정:",
        f"offset={SIGN_Y_Z_TOTAL_OFFSET:.3f},",
        f"interp={SIGN_Y_INTERPOLATION_LENGTH:.3f}mm",
    )

    metadata = helper.write_dsr_output(scaled_motions, output_py_path)
    print(f"사인용 출력 파일 생성 완료: {output_py_path}")
    return metadata


def main(args=None):
    selected_pen_name = DEFAULT_PEN
    if args and len(args) > 0:
        selected_pen_name = args[0]
    elif len(sys.argv) > 1:
        selected_pen_name = sys.argv[1]

    print(f"사용 사인 G-code 파일: {SIGN_NC_PATH}")
    print(f"생성 출력 파일: {SIGN_OUTPUT_PY}")
    print(f"선택 펜: {selected_pen_name}")
    print(f"고정 사인 좌표: ({SIGN_DRAW_CX}, {SIGN_DRAW_CY})")
    print(f"사인 축소 비율: {SIGN_SCALE_FACTOR}")
    print(
        f"사인 Y-Z 보정 설정: offset={SIGN_Y_Z_TOTAL_OFFSET}, "
        f"interp={SIGN_Y_INTERPOLATION_LENGTH}"
    )

    if not os.path.exists(SIGN_NC_PATH):
        raise FileNotFoundError(f"사인 G-code 파일이 없습니다: {SIGN_NC_PATH}")

    rclpy.init(args=[] if args is None else args)
    node = rclpy.create_node("robot_sign_py", namespace=helper.ROBOT_ID)
    helper.DR_init.__dsr__node = node

    time.sleep(2)

    try:
        from DSR_ROBOT2 import (
            ROBOT_MODE_AUTONOMOUS,
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
        rclpy.shutdown()
        return

    selected_key = selected_pen_name.strip().lower()
    selected_tcp = helper.PEN_TCP_MAP.get(selected_key)
    if selected_tcp is None:
        valid_names = ", ".join(sorted(helper.PEN_TCP_MAP.keys()))
        raise ValueError(
            f"지원하지 않는 펜 이름입니다: '{selected_pen_name}'. 가능한 값: {valid_names}"
        )

    selected_pick = helper.PEN_PICK_CONFIG[selected_tcp]
    requested_tcp_name = helper.DRAW_TCP_NAME_MAP.get(selected_tcp, selected_tcp)

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

    def normalize_tcp_name(name):
        return str(name).strip().lower()

    def set_tcp_with_verify(target_tcp, retries=2):
        current_tcp = ""
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
            if normalize_tcp_name(current_tcp) == normalize_tcp_name(target_tcp):
                return current_tcp

        raise RuntimeError(
            f"TCP 변경 실패: requested='{target_tcp}', current='{current_tcp}'. "
            "티칭펜던트 TCP 이름(대소문자/철자)을 확인하세요."
        )

    def resolve_pen_key_from_tcp_name(tcp_name):
        normalized_tcp = normalize_tcp_name(tcp_name)
        for pen_key, mapped_tcp_name in helper.DRAW_TCP_NAME_MAP.items():
            if normalize_tcp_name(mapped_tcp_name) == normalized_tcp:
                return pen_key
        return None

    def resolve_cz_value(default_pen_key):
        current_tcp_name = get_tcp()
        current_pen_key = resolve_pen_key_from_tcp_name(current_tcp_name)
        pen_key = current_pen_key or default_pen_key
        if pen_key not in helper.PEN_CZ_MAP:
            raise KeyError(f"cz 값이 정의되지 않은 펜 타입입니다: {pen_key}")
        logger.info(
            f"cz 설정: tcp='{current_tcp_name}', pen_key='{pen_key}', cz={helper.PEN_CZ_MAP[pen_key]}"
        )
        return helper.PEN_CZ_MAP[pen_key]

    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    pick_pos_a = posj(*selected_pick["pick_pos_a"])
    pick_pos_b = posj(*selected_pick["pick_pos_b"])
    pick_pose_down = posx(*selected_pick["pick_pose_down"])
    pick_pose_up = posx(*selected_pick["pick_pose_up"])
    camera_pos = posj(*CAMERA_POS_JOINT)
    q_init = posj(*DRAW_READY_JOINT)

    generate_sign_output(SIGN_NC_PATH, SIGN_OUTPUT_PY)
    output_linear_sign = helper.load_draw_module("output_linear_sign_main", SIGN_OUTPUT_PY)

    print("\n=== 1. 펜 집기 작업 시작 ===")
    set_tcp_with_verify(helper.BASE_TCP_NAME)
    open_gripper()
    movesj([pick_pos_a, pick_pos_b], vel=50, acc=50)
    movel(pick_pose_up, vel=100, acc=100)
    movel(pick_pose_down, vel=100, acc=100)
    close_gripper()
    movel(pick_pose_up, vel=100, acc=100)

    print(f"\n=== 2. TCP 설정 ({requested_tcp_name}) ===")
    set_tcp_with_verify(requested_tcp_name)

    print("\n=== 3. 사인 그리기 시작 ===")
    movej(q_init, vel=80, acc=80)

    pen_rpy = (0.0, 180.0, 90.0)
    cz = resolve_cz_value(selected_tcp) - 1.3

    output_linear_sign.draw(SIGN_DRAW_CX, SIGN_DRAW_CY, cz)
    movel(
        posx(SIGN_DRAW_CX, SIGN_DRAW_CY, cz + SIGN_LIFT_MM, *pen_rpy),
        vel=50,
        acc=50,
    )

    print("\n=== 4. 펜 반납 ===")
    set_tcp_with_verify(helper.BASE_TCP_NAME)
    movesj([pick_pos_a, pick_pos_b], vel=50, acc=50)
    movel(pick_pose_up, vel=100, acc=100)
    movel(pick_pose_down, vel=100, acc=100)
    open_gripper()
    movel(pick_pose_up, vel=100, acc=100)
    movej(camera_pos, vel=30, acc=30)
    close_gripper()

    print("\n=== 사인 작업 완료 ===")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
