import plyfile
import numpy as np
import open3d as o3d


'''
---plydata---
ply
format binary_little_endian 1.0
comment Created by Open3D
element vertex 752131
property double x
property double y
property double z
property double nx
property double ny
property double nz
property uchar red
property uchar green
property uchar blue
element face 1491574
property list uchar uint vertex_indices
end_header

---plydata.elements[0].data[0]---
(4.17526996, 2.22874256, 1.28829702, -0.37908478, -0.35694789, -0.85374641, 192, 192, 128)

---plydata['vertex']---
element vertex 752131
property double x
property double y
property double z
property double nx
property double ny
property double nz
property uchar red
property uchar green
property uchar blue

---plydata['vertex'].data[0]---
(4.17526996, 2.22874256, 1.28829702, -0.37908478, -0.35694789, -0.85374641, 192, 192, 128)
'''

in_filename = "smesh002000.ply"
out_filename = "nsmesh.ply"


def print_new_model():
    with open(in_filename, "rb") as f:
        plydata = plyfile.PlyData.read(f)
        print('---plydata---')
        print(plydata)
        print()
        print('---plydata.elements[0].data[0]---')
        print(plydata.elements[0].data[0])
        print()
        print("---plydata['vertex']---")
        print(plydata['vertex'])
        print()
        print("---plydata['vertex'].data[0]---")
        print(plydata['vertex'].data[0])


def read_ply(filename):
    plydata = plyfile.PlyData.read(filename)
    pc = plydata['vertex'].data
    pc_array = np.array([[x, y, z, nx, ny, nz, r, g, b] for x, y, z, nx, ny, nz, r, g, b in pc])
    return pc_array


def update_camera(vis):
    ctr = vis.get_view_control()
    camera_params = ctr.convert_to_pinhole_camera_parameters()
    print(camera_params.intrinsic.intrinsic_matrix)
    print(camera_params.extrinsic)


def print_img(filename):

    pcd = o3d.io.read_point_cloud(filename)
    print(pcd)
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()


if __name__ == '__main__':
    file_name = 'checkpoints/cmesh005000.ply'
    print_img(file_name)
