import cv2
import freenect
import numpy as np
import open3d as o3d
import time

# ---------- Parámetros cámara (Kinect v1 aprox) ----------
width, height = 640, 480
fx, fy = 525.0, 525.0
cx, cy = width / 2.0, height / 2.0

camera_intrinsics = o3d.camera.PinholeCameraIntrinsic(
    width, height, fx, fy, cx, cy
)

# ---------- Modelo detección ----------
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
    volume = o3d.pipelines.integration.ScalableTSDFVolume(
        voxel_length=0.02,
        sdf_trunc=0.04,
        color_type=o3d.pipelines.integration.TSDFVolumeColorType.RGB8
    )

    cam_pose = np.eye(4)
    prev_rgbd = None
    first = True

    vis = o3d.visualization.Visualizer()
    vis.create_window("Mapa 3D (TSDF)", 800, 600)
    pcd_vis = None
    last_update = time.time()

    while True:
        rgb, depth_m = get_rgb_depth()
        (h, w) = rgb.shape[:2]

        # ---- SLAM ----
        rgb_o3d = o3d.geometry.Image(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))
        depth_o3d = o3d.geometry.Image((depth_m * 1000.0).astype(np.uint16))

        rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
            rgb_o3d,
            depth_o3d,
            depth_scale=1000.0,
            depth_trunc=3.5,
            convert_rgb_to_intensity=False
        )

        if first:
            volume.integrate(rgbd, camera_intrinsics, cam_pose)
            prev_rgbd = rgbd
            first = False
        else:
            success, odo_init = o3d.pipelines.odometry.compute_rgbd_odometry(
                rgbd,
                prev_rgbd,
                camera_intrinsics,
                np.eye(4),
                o3d.pipelines.odometry.RGBDOdometryJacobianFromHybridTerm(),
                o3d.pipelines.odometry.OdometryOption()
            )

            if success:
                cam_pose[:] = cam_pose @ np.linalg.inv(odo_init)
                volume.integrate(rgbd, camera_intrinsics, cam_pose)
                prev_rgbd = rgbd

        # ---- Detección personas ----
        blob = cv2.dnn.blobFromImage(
            cv2.resize(rgb, (300, 300)),
            0.007843,
            (300, 300),
            127.5
        )
        net.setInput(blob)
        detections = net.forward()

        person_world_positions = []

        for i in range(detections.shape[2]):
            conf = detections[0, 0, i, 2]
            if conf < 0.5:
                continue

            idx = int(detections[0, 0, i, 1])
            if idx >= len(CLASSES):
                continue
            label = CLASSES[idx]
            if label != "person":
                conti
