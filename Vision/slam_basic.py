import cv2
import freenect
import numpy as np
import open3d as o3d
import time

# Parámetros aproximados del Kinect v1
width, height = 640, 480
fx, fy = 525.0, 525.0
cx, cy = width / 2.0, height / 2.0

camera_intrinsics = o3d.camera.PinholeCameraIntrinsic(
    width, height, fx, fy, cx, cy
)


def get_rgb_depth():
    rgb, _ = freenect.sync_get_video()
    depth_raw, _ = freenect.sync_get_depth()

    rgb = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    depth_raw = depth_raw.astype(np.float32)

    # modelo típico Kinect -> metros
    depth_m = 0.1236 * np.tan(depth_raw / 2842.5 + 1.1863)

    return rgb, depth_m


def main():
    print("Iniciando mini-SLAM con Kinect... (pulsa 'q' para salir)")

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

    try:
        while True:
            rgb, depth_m = get_rgb_depth()

            cv2.imshow("Kinect RGB", rgb)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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
                continue

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

            if time.time() - last_update > 1.0:
                pcd = volume.extract_point_cloud()
                if pcd_vis is None:
                    pcd_vis = pcd
                    vis.add_geometry(pcd_vis)
                else:
                    pcd_vis.points = pcd.points
                    pcd_vis.colors = pcd.colors
                    vis.update_geometry(pcd_vis)

                vis.poll_events()
                vis.update_renderer()
                last_update = time.time()

    finally:
        print("Extrayendo nube de puntos final...")
        pcd = volume.extract_point_cloud()
        o3d.io.write_point_cloud("mapa_kinect.pcd", pcd)
        print("Mapa guardado como mapa_kinect.pcd")

        vis.destroy_window()
        cv2.destroyAllWindows()
        freenect.sync_stop()


if __name__ == "__main__":
    main()
