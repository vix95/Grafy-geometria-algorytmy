from matplotlib import pyplot as plt
from Point import Point
from SegmentType import SegmentType
import numpy as np

PRINT_ANNOTATE = False


def import_file(filename):
    point_list = []

    with open(filename, "r") as f:
        for line in f.readlines():
            tmp = line.strip().split(", ")
            point = Point(
                segment_id=int(tmp[0]),
                x=float(tmp[1]),
                y=float(tmp[2]),
                is_start=tmp[3] == "True",
                segment_type=eval(tmp[4]))
            point_list.append(point)

    return point_list


def draw_plot(area):
    x = [point.x for point in area.points]
    y = [point.y for point in area.points]

    # area.ax.scatter(x, y, s=20, color="k")

    if PRINT_ANNOTATE:
        for i, point in enumerate(area.points):
            area.ax.annotate(point, (x[i] + 0.02, y[i] + 0.04), fontsize=12)

    for i in range(0, len(area.points), 2):
        p1 = area.points[i]
        p2 = area.points[i + 1]
        area.ax.plot([p1.x, p2.x], [p1.y, p2.y], color="black", linewidth=3)

    area.ax.margins(x=0.2, y=0.2)
    plt.xticks(np.arange(area.X_PLOT_SIZE_MIN, area.X_PLOT_SIZE_MAX + 1, 1.0))
    plt.yticks(np.arange(area.Y_PLOT_SIZE_MIN, area.Y_PLOT_SIZE_MAX + 1, 1.0))


def draw_intersections(area):
    x = [point.x for point in area.intersections]
    y = [point.y for point in area.intersections]

    area.ax.scatter(x, y, s=40, color="red", zorder=10)
    plt.xticks(np.arange(area.X_PLOT_SIZE_MIN, area.X_PLOT_SIZE_MAX + 1, 1.0))
    plt.yticks(np.arange(area.Y_PLOT_SIZE_MIN, area.Y_PLOT_SIZE_MAX + 1, 1.0))


def set_title(area, tree):
    area.fig.suptitle(f"Count of crossed segments: {tree.crossed_qty}", fontsize=16)
