"""
    - importowanie danych z plików
    - rysowanie plota
    - zaznaczanie obszarów
    - generowanie losowych punktów
"""

import random
from Point import *
from matplotlib import pyplot as plt


def import_file(filename):
    point_list = []

    with open(filename, 'r') as f:
        d = [list(map(int, coord.strip().split(' '))) for coord in f.readlines()]

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


def draw_plot(obj, to_find):
    x = [point.x for point in obj.points["all"]]
    y = [point.y for point in obj.points["all"]]

    obj.ax.scatter(x, y, s=100, color='k')
    obj.ax.axis("off")

    for i, point in enumerate(obj.points["all"]):
        obj.ax.annotate(point.get_xy(), (x[i] + 0.02, y[i] + 0.04), fontsize=20)

    obj.ax.margins(x=0.2, y=0.2)
    plt.xlim([-.1, obj.plot_max_size + .1])
    plt.ylim([-.1, obj.plot_max_size + .1])
    draw_rectangle(obj)

    left_bottom = (to_find.min.get_x(), to_find.min.get_y())
    x_size = to_find.max.get_x() - to_find.min.get_x()
    y_size = to_find.max.get_y() - to_find.min.get_y()
    rect = plt.Rectangle(left_bottom, x_size, y_size, color='r', alpha=.2)
    obj.ax.add_patch(rect)


def color_solution(obj):
    if obj.points.get("solution") is not None:
        x = [point.x for point in obj.points["solution"]]
        y = [point.y for point in obj.points["solution"]]
        obj.ax.scatter(x, y, s=100, color='r')


def draw_rectangle(obj):
    for node in obj.tree.in_order():
        if not node.is_root:
            left_bottom = (node.area.min.x, node.area.min.y)
            x_size = node.area.max.x - left_bottom[0]
            y_size = node.area.max.y - left_bottom[1]
            rect = plt.Rectangle(left_bottom, x_size, y_size, color='k', fill=None, alpha=1, lw=1)
            obj.ax.add_patch(rect)

            if node.xy == 0 and node.is_leaf:
                x_size = abs(node.area.min.x - node.point.get_x())
                rect = plt.Rectangle(left_bottom, x_size, y_size, color='k', fill=None, alpha=1, lw=1)
                obj.ax.add_patch(rect)
            elif node.xy == 1 and node.is_leaf:
                y_size = abs(node.area.min.y - node.point.get_y())
                rect = plt.Rectangle(left_bottom, x_size, y_size, color='k', fill=None, alpha=1, lw=1)
                obj.ax.add_patch(rect)


def generate_random_points(qty):
    points = []
    for i in range(qty):
        points.append(Point(round(random.randint(0, 10), 1), round(random.randint(0, 10), 1)))

    return points
