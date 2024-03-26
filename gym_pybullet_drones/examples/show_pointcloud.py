import os
import open3d as o3d
import numpy as np

path = r"results/pointcloud_03.26.2024_23.38.35drone_0/"
data = []
for filename in os.listdir(path):
    data_tmp = np.load(os.path.join(path,filename))
    data.append(data_tmp)
data = np.concatenate(data)
pcd = o3d.geometry.PointCloud()

# print('Displaying input point cloud ...')
pcd.points = o3d.utility.Vector3dVector(data)
o3d.visualization.draw_geometries([pcd])

# print('Displaying voxel grid ...')
# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.5)
# o3d.visualization.draw([voxel_grid])
# print(voxel_grid.get_axis_aligned_bounding_box())