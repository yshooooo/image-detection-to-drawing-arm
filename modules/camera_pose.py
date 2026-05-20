import rclpy
import time

from rclpy.logging import get_logger

ROBOT_ID = "dsr01"
ROBOT_MODEL = "a0509"

import DR_init

DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL

logger = get_logger("camera_pose_logger")

CAMERA_POS_J_1 = (-90.19, 6, -132.50, 10, 54.36, 2.15)
CAMERA_POS_J_2 = (-90.19, -9.74, -132.50, -2.28, 54.36, 2.15)


def main(args=None):
    rclpy.init(args=[] if args is None else args)
    node = rclpy.create_node("camera_pose_py", namespace=ROBOT_ID)
    DR_init.__dsr__node = node
    time.sleep(1.0)

    try:
        from DSR_ROBOT2 import get_current_posj, movesj, posj
    except ImportError as exc:
        print(f"Error importing DSR_ROBOT2 : {exc}")
        rclpy.shutdown()
        return

    target_1 = posj(*CAMERA_POS_J_1)
    target_2 = posj(*CAMERA_POS_J_2)

    movesj([target_1, target_2], vel=50, acc=50)

    cur, _ = get_current_posj()
    logger.info(f"camera_pos_j target={CAMERA_POS_J_2}")
    logger.info(f"current_posj={tuple(round(v, 3) for v in cur)}")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
