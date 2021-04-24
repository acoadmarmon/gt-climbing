
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

import matplotlib as mpl

import numpy as np
import matplotlib.pyplot as plt
import random


def points_from_image():

    points = [[513, 32, 0.0], [575, 92, 0.0], [535, 119, 0.0], [511, 72, 0.0], [500, 105, 0.0],
              [485, 74, 0.0], [486, 49, 0.0], [446, 88, 0.0], [421, 59, 0.0], [425, 113, 0.0], [416, 105, 0.0],
              [457, 144, 0.5], [511, 173, 1.1], [447, 173, 1.1], [379, 81, -0.4], [319, 81, -0.4], [339, 92, -0.8],
              [319, 111, -0.9], [295, 103, -0.1], [281, 94, 0.1], [282, 123, 1.0],
              [376, 123, -0.1], [321, 129, 0.0], [300, 150, 1.0], [318, 164, 1.9], [348, 159, 1.4], [375, 179, 1.8],
              [386, 145, 1.0], [353, 227, 2.0], [311, 270, 2.0], [256, 224, 2.0], [230, 263, 2.0],
              [425, 203, 1.6], [489, 229, 1.1], [427, 271, 1.5], [369, 286, 1.8], [431, 325, 1.4],
              [525,207, 0.8], [541, 237, 0.9], [596, 193, 0.4], [600, 264, 0.75],
              [564, 293, 1.0], [510, 242, 1.0], [498, 276, 1.0],
              [594, 326, 0.8], [426, 355, 1.3], [388, 347, 1.6], [376, 371, 1.0],
              [489, 371, 0.5], [469, 360, 0.8],
              [326, 326, 1.9], [316, 367, 1.4], [303, 335, 1.7], [283, 364, 1.3], [251, 323, 1.5], [257, 293, 2.0],
              [205, 279, 1.8], [231, 341, 1.5], [198, 316, 1.6], [207, 387, 1.2],
              [265, 155, 1.9], [252, 136, 1.6], [254, 109, 1.3], [242, 92, 0.4], [228, 135, 0.75],
              [208, 123, 0.4], [186, 108, 0.8], [180, 145, 0.2], [149, 128, 0.6], [141, 160, 0.8], [228, 168, 1.0],
              [229, 191, 1.9], [189, 229, 1.9], [195, 178, 0.5], [166, 261, 1.9], [170, 353, 0.0], [139, 312, 0.5],
              [120, 356, 0.4], [73, 341, 1.0], [76, 382, 1.0], [33, 405, 0.4], [65, 299, 1.0], [39, 284, 1.0],
              [156, 165, 0.5], [147, 224, 1.5], [127, 201, 1.0], [122, 127, 1.0], [120, 161, 1.1], [101, 184, 1.3],
              [109, 236, 1.2], [111, 277, 1.0], [80, 275, 1.1], [74, 228, 1.5], [87, 133, 1.4], [61, 154, 1.75],
              [37, 142, 1.5], [43, 211, 1.6], [25, 187, 1.0], [10, 188, 0.0], [22, 285, 0.75], [13, 309, 0.5],
              [14, 244, 0.5], [20, 360, 0.5], [29, 324, 0.8]]

    points = np.array(points)

    # scale for 4ft long arms
    points[:, 0] = points[:, 0] / (616/30)  # 616 -> 30
    points[:, 1] = points[:, 1] / (423/10)  # 423 - > 10
    points[:, 2] = points[:, 2]  # 3 (-1 - 2ft )

    return points


def get_random_points(num_points):

    # robots arms are 2ft long - 1ft per link

    points = []
    for pt in range(num_points):

        # climbing wall = 10ft X 30ft, at most 1.5 ft change in z axis
        rand_x = random.randrange(0, 100)
        rand_y = random.randrange(0, 300)
        rand_z = random.randrange(0, 10)

        # randrange needed intergers, but divide to get better data

        rand_x = rand_x / 10
        rand_y = rand_y / 10
        rand_z = rand_z / 10

        points.append([rand_x, rand_y, rand_z])

    points = np.array(points)
    return points


def plot_points(points):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x_scale = 0.68
    y_scale = 1.0
    z_scale = 0.0048 * 100

    # x_scale = 1.0
    # y_scale = 1.0
    # z_scale = 1.0

    scale = np.diag([x_scale, y_scale, z_scale, 1.0])
    scale = scale * (1.0 / scale.max())
    scale[3, 3] = 1.0

    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)

    ax.get_proj = short_proj

    ax.scatter(points[:, 1], points[:, 0], points[:, 2], marker='o')

    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')

    # ax.view_init(elev, azimuth angle)
    ax.view_init(90, -90)

    plt.show()


if __name__ == "__main__":
    # points = get_random_points(50)
    points = points_from_image()
    plot_points(points)
