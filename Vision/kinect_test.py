import cv2
import freenect
import numpy as np


# ---------- Functions to read from the Kinect ----------

def get_video():
    frame, _ = freenect.sync_get_video()
    # Kinect provides RGB, while OpenCV uses BGR
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame_bgr


def get_depth():
    depth, _ = freenect.sync_get_depth()
    # depth is a 11-bit array, normalized for visualization purposes
    depth_uint8 = depth.astype(np.uint8)
    return depth_uint8


# ---------- Main Program ----------

def main():
    print("Iniciando lectura del Kinect... (presiona 'q' para salir)")
    while True:
        frame_color = get_video()
        frame_depth = get_depth()

        cv2.imshow("Kinect RGB", frame_color)
        cv2.imshow("Kinect Depth", frame_depth)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    freenect.sync_stop()


if __name__ == "__main__":
    main()

