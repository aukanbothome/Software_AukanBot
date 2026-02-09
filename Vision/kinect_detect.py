import cv2
import freenect
import numpy as np
import time

# Paths to the model files (adjust if located in a different directory)
PROTO_PATH = "MobileNetSSD_deploy.prototxt"
MODEL_PATH = "MobileNetSSD_deploy.caffemodel"

# Classes recognized by the model
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]


def get_video():
    frame, _ = freenect.sync_get_video()
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame_bgr


print("[INFO] Cargando red neuronal...")
net = cv2.dnn.readNetFromCaffe(PROTO_PATH, MODEL_PATH)
print("[INFO] Red cargada.")


def main():
    print("Iniciando detección con Kinect... (pulsa 'q' para salir)")
    fps_time = time.time()
    frame_count = 0

    while True:
        frame = get_video()
        (h, w) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300, 300)),
            0.007843,
            (300, 300),
            127.5
        )

        net.setInput(blob)
        detections = net.forward()

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
                print("Persona detectada con confianza:", confidence)

        # FPS
        frame_count += 1
        if frame_count >= 10:
            now = time.time()
            fps = frame_count / (now - fps_time)
            fps_time = now
            frame_count = 0
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 255), 2)

        cv2.imshow("Kinect + Detección", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    freenect.sync_stop()


if __name__ == "__main__":
    main()

