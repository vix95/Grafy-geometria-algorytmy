from Point import Point
from matplotlib import pyplot as plt
import numpy as np


def import_file(filename):
    point_list = []

    with open(filename, "r") as f:
        for line in f.readlines():
            tmp = line.strip().split(" ")
            point = Point(x=float(tmp[0]), y=float(tmp[1]))
            point_list.append(point)

    return point_list


def draw_plot(area):
    x = [point.x for point in area.point_list]
    y = [point.y for point in area.point_list]

    area.ax.scatter(x, y, s=3, color="k")

    for i, point in enumerate(area.point_list):
        area.ax.annotate(point, (x[i] - .45, y[i] + .2), fontsize=5)


def draw_circles(area):
    for hospital in area.hospital_list:
        area.ax.scatter(hospital.x, hospital.y, s=3, color="r")
        c = plt.Circle((hospital.x, hospital.y), area.opt_dist, color="r", linestyle='--', fill=False, linewidth=.5)
        plt.gcf().gca().add_artist(c)


def plt_setup(area):
    plt.xticks(np.arange(area.X_PLOT_SIZE_MIN - area.opt_dist - 1, area.X_PLOT_SIZE_MAX + area.opt_dist + 1, 2))
    plt.yticks(np.arange(area.Y_PLOT_SIZE_MIN - area.opt_dist - 1, area.Y_PLOT_SIZE_MAX + area.opt_dist + 1, 2))
    plt.axis("off")
