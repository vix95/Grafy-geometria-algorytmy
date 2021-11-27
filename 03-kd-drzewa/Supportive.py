"""
    - importowanie danych z plikow
    - rysowanie plota
"""

import random
from copy import deepcopy

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
        obj.ax.annotate(point.get_xy(), (x[i] + 0.02, y[i] + 0.04), fontsize=12)

    obj.ax.margins(x=0.2, y=0.2)
    plt.xlim([.1, obj.max_size - .1])
    plt.ylim([.1, obj.max_size - .1])
    draw_lines(obj)

    rect = plt.Rectangle((to_find.min.get_x(), to_find.min.get_y()),
                         to_find.max.get_x() - to_find.min.get_x(),
                         to_find.max.get_y() - to_find.min.get_y(),
                         color='r', alpha=.2)
    #obj.ax.add_patch(rect)


def draw_lines(obj):
    for node in obj.tree.in_order():
        if not node.is_root and not node.is_leaf:
            obj.ax.plot([node.area.max[0], node.area.max[0]], [node.area.min[1], node.area.max[1]], color='k', lw=1)
            obj.ax.plot([node.area.min[0], node.area.min[0]], [node.area.min[1], node.area.max[1]], color='k', lw=1)
            obj.ax.plot([node.area.min[0], node.area.max[0]], [node.area.min[1], node.area.min[1]], color='k', lw=1)
            obj.ax.plot([node.area.min[0], node.area.max[0]], [node.area.max[1], node.area.max[1]], color='k', lw=1)


def assign_areas(node):
    if not node.is_leaf:
        if node.parent:
            parent = node.parent
            split = parent.median
            node.area = parent.area
            area = deepcopy(node.area)

            if None not in (area, split):
                if node.xy == 1:
                    if node.is_left:
                        area.max[0] = split
                    else:
                        area.min[0] = split
                else:
                    if node.is_left:
                        area.max[1] = split
                    else:
                        area.min[1] = split
                node.area = area

        if node.left:
            assign_areas(node.left)
        if node.right:
            assign_areas(node.right)
