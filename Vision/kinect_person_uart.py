import cv2
import freenect
import numpy as np
import time
import serial

# ---------- UART CONFIGURATION ----------
ser = serial.Serial("/dev/serial0", 115200, timeout=1)
time.sleep(2)


def enviar_uart(msg: str):
    ser.write((msg + "\n").encode('utf-8'))
    print("[UART] Enviado:", msg)


# ---------- SAFE DISTANCE ----------
SAFE_DISTANCE_M = 1.2
already_stopped = False
already_greeted = False

# ---------- DETECTION MODEL ----------
PROTO_PATH = "MobileNetSSD_deploy.prototxt"
MODEL_PATH = "MobileNetSSD_deploy.caffemodel"

CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

print("[INFO] Cargando red neuronal...")
net = cv2.dnn.readNetFromCaffe(PROTO_PATH, MODEL_PATH)
print("[INFO] Red cargada.")


def get_rgb_depth():
    rgb, _ = freenect.sync_get_video()
    depth_raw, _ = freenect.sync_get_depth()

    rgb_bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    depth_raw = depth_raw.astype(np.float32)
    depth_m = 0.1236 * np.tan(depth_raw / 2842.5 + 1.1863)

    return rgb_bgr, depth_m


def main():
    global already_stopped, already_greeted

    print("Iniciando detección + distancia + UART (q para salir)")

    while True:
        frame, depth_m = get_rgb_depth()
        (h, w) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300, 300)),
            0.007843,
            (300, 300),
            127.5
        )
        net.setInput(blob)
        detections = net.forward()

        min_person_dist = None

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence < 0.5:
                continue

            idx = int(detections[0, 0, i, 1])
            if idx >= len(CLASSES):
                continue
            label = CLASSES[idx]

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            text = f"{label}: {confidence:.2f}"
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          (0, 255, 0), 2)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

            if label == "person":
                cx = int((startX + endX) / 2)
                cy = int((startY + endY) / 2)
                cx = np.clip(cx, 0, w - 1)
                cy = np.clip(cy, 0, h - 1)

                dist = depth_m[cy, cx]
                if np.isfinite(dist) and dist > 0:
                    d_text = f"{dist:.2f} m"
                    cv2.putText(frame, d_text, (cx, cy),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 255, 255), 2)

                    if (min_person_dist is None) or (dist < min_person_dist):
                        min_person_dist = dist

        # ---- SAFETY LOGIC ----
        if min_person_dist is not None:
            print(f"Persona más cercana a: {min_person_dist:.2f} m")

            if (min_person_dist < SAFE_DISTANCE_M) and (not already_stopped):
                enviar_uart("STOP_BASE")
                already_stopped = True

            if (0.7 < min_person_dist < SAFE_DISTANCE_M + 0.1) and (not already_greeted):
                enviar_uart("SALUDAR")
                already_greeted = True
        else:
            already_stopped = False
            already_greeted = False

        cv2.imshow("Kinect + Detección + Distancia", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    freenect.sync_stop()
    ser.close()


if __name__ == "__main__":
    main()

