from matplotlib import pyplot as plt
from Area import Point
import numpy as np


def import_file(filename):
    edge_list = []

    with open(filename, 'r') as f:
        for coord in f.readlines():
            tmp = coord.strip().split(";")
            p1 = tuple(map(float, tmp[0].split(",")))
            p2 = tuple(map(float, tmp[1].split(",")))
            edge_list.append([p1, p2])

    return edge_list


def draw_plot(area):
    x = [point.x for point in area.C_points]
    y = [point.y for point in area.C_points]

    # area.ax.scatter(x, y, s=20, color='k')

    for i, point in enumerate(area.C_points):
        area.ax.annotate(point, (x[i] + 0.02, y[i] + 0.04), fontsize=12)

    for i, pair in enumerate(area.points):
        p1 = Point(x=pair[0][0], y=pair[0][1])
        p2 = Point(x=pair[1][0], y=pair[1][1])
        area.ax.plot([p1.x, p2.x], [p1.y, p2.y], color="black", linewidth=3)

    area.ax.margins(x=0.2, y=0.2)
    plt.xticks(np.arange(0, area.X_PLOT_SIZE + 1, 1.0))
    plt.yticks(np.arange(0, area.Y_PLOT_SIZE + 1, 1.0))


def draw_line(area):
    plt.axvline(x=area.line, linewidth=2, linestyle="dashed", color="red")


def draw_intersections(area):
    x = [point.x for point in area.intersections]
    y = [point.y for point in area.intersections]

    area.ax.scatter(x, y, s=40, color="red", zorder=10)
    plt.xticks(np.arange(0, area.X_PLOT_SIZE + 1, 1.0))
    plt.yticks(np.arange(0, area.Y_PLOT_SIZE + 1, 1.0))

