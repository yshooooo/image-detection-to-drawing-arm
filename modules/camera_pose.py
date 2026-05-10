import rclpy
import time

from rclpy.logging import get_logger

ROBOT_ID = "dsr01"
ROBOT_MODEL = "a0509"

import DR_init

DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL

logger = get_logger("camera_pose_logger")

CAMERA_POS_J = (-90.19, -9.74, -132.50, -2.28, 54.36, 2.15)


def main(args=None):
    rclpy.init(args=[] if args is None else args)
    node = rclpy.create_node("camera_pose_py", namespace=ROBOT_ID)
    DR_init.__dsr__node = node
    time.sleep(1.0)

    try:
        from DSR_ROBOT2 import get_current_posj, movej, posj
    except ImportError as exc:
        print(f"Error importing DSR_ROBOT2 : {exc}")
        rclpy.shutdown()
        return

    target = posj(*CAMERA_POS_J)
    movej(target, vel=30, acc=30)

    cur, _ = get_current_posj()
    logger.info(f"camera_pos_j target={CAMERA_POS_J}")
    logger.info(f"current_posj={tuple(round(v, 3) for v in cur)}")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
