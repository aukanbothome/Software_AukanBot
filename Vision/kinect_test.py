import cv2
import freenect
import numpy as np


# ---------- Funciones para leer del Kinect ----------

def get_video():
    frame, _ = freenect.sync_get_video()
    # El Kinect entrega RGB, OpenCV usa BGR
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame_bgr


def get_depth():
    depth, _ = freenect.sync_get_depth()
    # depth es un array de 11 bits, lo normalizamos para verlo
    depth_uint8 = depth.astype(np.uint8)
    return depth_uint8


# ---------- Programa principal ----------

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
