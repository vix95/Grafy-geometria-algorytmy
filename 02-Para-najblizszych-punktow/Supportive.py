import random

from Point import *
from matplotlib import pyplot as plt


def import_file(filename):
    point_list = []

    with open(filename, 'r') as f:
        d = [list(map(float, coord.strip().split(' '))) for coord in f.readlines()]

    for coordinates in d:
        if len(coordinates) == 2:
            if len(point_list) > 0:
                point_list.append(Point(coordinates[0], coordinates[1]))
            else:
                point_list.append(Point(coordinates[0], coordinates[1]))
        else:
            print("[{}] Removed value: {}".format(filename, coordinates))

    for i, point in enumerate(point_list):
        if point == point_list[-1]:
            point.next_p = point_list[0]
        else:
            point.next_p = point_list[i + 1]

    return point_list


def draw_plot(area):
    x = [point.x for point in area.points["all"]]
    y = [point.y for point in area.points["all"]]

    area.ax.scatter(x, y, s=20, color='k')

    for i, point in enumerate(area.points["all"]):
        area.ax.annotate(point.get_xy(), (x[i] + 0.02, y[i] + 0.04), fontsize=12)

    area.ax.margins(x=0.2, y=0.2)


def draw_line(area):
    plt.axvline(x=area.middle_point.get_x(), linewidth=2, linestyle="dashed", color="black")
    plt.axvline(x=area.middle_point.get_x() - area.min_s1_s2_distance, linewidth=1, linestyle="dashed", color="black")
    plt.axvline(x=area.middle_point.get_x() + area.min_s1_s2_distance, linewidth=1, linestyle="dashed", color="black")


def draw_points_connection(area):
    draw_connection(area, area.s1_min.get("p1"), area.s1_min.get("p2"), "blue")
    draw_connection(area, area.s2_min.get("p1"), area.s2_min.get("p2"), "red")

    if area.s3_min.get("p1") is not None and area.s3_min.get("p2") is not None:
        draw_connection(area, area.s3_min.get("p1"), area.s3_min.get("p2"), "green")


def draw_connection(area, p1, p2, color):
    area.ax.plot([p1.get_x(), p2.get_x()],
                 [p1.get_y(), p2.get_y()],
                 color=color, linewidth=3)


def show_results(area):
    if area.s3_min.get("p1") is not None and area.s3_min.get("p2") is not None:
        plt.title("Minimal distance: {}\nS1: {} {}\nS2: {} {}\nS3: {} {}".
                  format(area.min_s1_s2_distance,
                         area.s1_min.get("p1").get_xy(), area.s1_min.get("p2").get_xy(),
                         area.s2_min.get("p1").get_xy(), area.s2_min.get("p2").get_xy(),
                         area.s3_min.get("p1").get_xy(), area.s3_min.get("p2").get_xy(),
                         fontsize=40))

    else:
        plt.title("Minimal distance: {}\nS1: {} {}\nS2: {} {}".
                  format(area.min_s1_s2_distance,
                         area.s1_min.get("p1").get_xy(), area.s1_min.get("p2").get_xy(),
                         area.s2_min.get("p1").get_xy(), area.s2_min.get("p2").get_xy(),
                         fontsize=40))


def generate_random_points(qty):
    points = []
    for i in range(qty):
        points.append(Point(round(random.uniform(0.0, 10.0), 1), round(random.uniform(0.0, 10.0), 1)))

    return points
