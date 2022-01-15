from matplotlib import pyplot as plt
from Point import Point
from Segment import Segment
from SegmentType import SegmentType
import numpy as np

PRINT_ANNOTATE = True


def import_file(filename):
    point_list = []
    segments = []

    with open(filename, "r") as f:
        row = 0
        for line in f.readlines():
            tmp = line.strip().split(", ")
            point = Point(
                segment_id=int(row / 2),
                x=float(tmp[0]),
                y=float(tmp[1]),
                is_start=row % 2 == 0)
            point_list.append(point)
            row += 1

            if row % 2 == 0:
                if point_list[row - 2].y == point_list[row - 1].y:
                    point_list[row - 2].segment_type = SegmentType.HORIZONTAL
                    point_list[row - 1].segment_type = SegmentType.HORIZONTAL
                else:
                    point_list[row - 2].segment_type = SegmentType.VERTICAL
                    point_list[row - 1].segment_type = SegmentType.VERTICAL

                segment = Segment(start=point_list[row - 2], end=point_list[row - 1],
                                  segment_index=point_list[row - 2].segment_id)
                segments.append(segment)
                point_list[row - 2].segment = segment
                point_list[row - 1].segment = segment

    return point_list, segments


def draw_plot(area):
    x = [point.x for point in area.points]
    y = [point.y for point in area.points]

    # area.ax.scatter(x, y, s=20, color="k")

    if PRINT_ANNOTATE:
        for i, point in enumerate(area.points):
            area.ax.annotate("S" + str(point.segment_id), (x[i] + 0.02, y[i] + 0.04), fontsize=12)

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
