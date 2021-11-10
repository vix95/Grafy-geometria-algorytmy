import copy
import math

import numpy as np

from Point import *
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon as poly


def import_file(filename):
    point_list = []

    with open(filename, 'r') as f:
        d = [list(map(int, coord.strip().split(' '))) for coord in f.readlines()]

    for coordinates in d:
        if len(coordinates) == 2:
            if len(point_list) > 0:
                point_list.append(Point(coordinates[0], coordinates[1], point_list[-1]))
            else:
                point_list.append(Point(coordinates[0], coordinates[1]))
        else:
            print("[{}] Removed value: {}".format(filename, coordinates))

    point_list[0].prev_p = point_list[-1]

    for i, point in enumerate(point_list):
        if point == point_list[-1]:
            point.next_p = point_list[0]
        else:
            point.next_p = point_list[i + 1]

    return point_list


def draw_plot(polygon):
    x = [point.x for point in polygon.points]
    y = [point.y for point in polygon.points]

    x.append(polygon.points[0].x)
    y.append(polygon.points[0].y)

    polygon.ax.plot(x, y, color='k', linewidth=3, alpha=0.5)
    polygon.ax.scatter(x, y, s=120, color='k')
    polygon.ax.axis("off")

    for i, point in enumerate(polygon.points):
        polygon.ax.annotate(point.get_xy(), (x[i] + 0.02, y[i] + 0.04), fontsize=20)

    polygon.ax.margins(x=0.2, y=0.2)


def draw_min_max(polygon):
    polygon.ax.scatter(polygon.max_p.x, polygon.max_p.y, s=240, color='r')
    polygon.ax.axhline(polygon.max_p.y, color='r', linestyle='-')
    polygon.ax.scatter(polygon.min_p.x, polygon.min_p.y, s=240, color='b')
    polygon.ax.axhline(polygon.min_p.y, color='b', linestyle='-')


def draw_perimeter(polygon):
    points = [[point.x, point.y] for point in polygon.perimeter_points]
    points.append(points[0])
    p = poly(points, facecolor='b', alpha=0.2)
    polygon.ax.add_patch(p)


def set_title(polygon):
    plt.title("Is Kernel: {}\nPerimeter: {}".format(polygon.is_kernel, polygon.perimeter), fontsize=40)


def check_orientation(polygon, fix_orientation=False):
    x0, y0 = polygon.points[0].prev_p.get_xy()  # prev
    x1, y1 = polygon.points[0].get_xy()  # current
    x2, y2 = polygon.points[0].next_p.get_xy()  # next
    matrix = np.array(
        [[x0, y0, 1],
         [x1, y1, 1],
         [x2, y2, 1]])
    sgn = np.linalg.det(matrix)
    if sgn > 0:
        polygon.is_oriented_ok = True

    if sgn <= 0 and fix_orientation:
        polygon.points.reverse()
        for point in polygon.points:
            temp_point = copy.copy(point)
            point.next_p = temp_point.prev_p
            point.prev_p = temp_point.next_p
            polygon.is_oriented_ok = True


def find_min_and_max(polygon):
    for point in polygon.points:
        x0, y0 = point.prev_p.get_xy()  # prev
        x1, y1 = point.get_xy()  # current
        x2, y2 = point.next_p.get_xy()  # next
        x3, y3 = point.next_p.next_p.get_xy()  # next next

        is_turn_right = (y1 - y0) * (x2 - x0) > (y2 - y0) * (x1 - x0)

        if is_turn_right:
            if y0 > y1 and y2 > y1:
                point.place = 'min'
                polygon.min_points.append(point)
            elif y0 >= y1 and y1 <= y2 < y3:
                point.place = 'min'
                polygon.min_points.append(point)
            elif y0 < y1 and y2 < y1:
                point.place = 'max'
                polygon.max_points.append(point)
            elif y0 <= y1 and y1 >= y2 > y3:
                point.place = 'max'
                polygon.max_points.append(point)

    polygon.calc_max()
    polygon.calc_min()


def is_kernel(polygon):
    if polygon.min_p.y >= polygon.max_p.y and len(polygon.points) > 2:
        print("[{}] Kernel; Is oriented: {}".format(polygon.name, polygon.is_oriented_ok))
        polygon.is_kernel = True
        if polygon.two_points_at_least():
            calc_perimeter(polygon)
    else:
        print("[{}] No Kernel; Is oriented: {}".format(polygon.name, polygon.is_oriented_ok))
        polygon.is_kernel = False


def calc_dist(curr_point, prev_point):
    return math.sqrt((curr_point.x - prev_point.x) ** 2 + (curr_point.y - prev_point.y) ** 2)


def calc_perimeter(polygon):
    perimeter = 0
    point_max = polygon.max_p  # start from the MAX
    point_min = polygon.min_p  # first point of the MIN
    curr_point = copy.copy(point_max.next_p)
    prev_point = copy.copy(point_max)
    checked_points = 0

    while checked_points != len(polygon.points):
        if curr_point.y >= point_max.y:  # if is equal or higher than MAX y
            if curr_point.y <= point_min.y:  # if is equal or smaller than MIN y
                perimeter += calc_dist(curr_point, prev_point)
            else:  # is higher than MIN y, need to be cut by blue line (MIN)
                if curr_point.y == point_min.y:
                    curr_point = Point(curr_point.x, point_min.y, None, curr_point.next_p)
                    if curr_point not in polygon.perimeter_points:
                        perimeter += calc_dist(curr_point, prev_point)
                elif curr_point.x == point_min.x:
                    curr_point = Point(curr_point.y, point_min.x, None, curr_point.next_p)
                    if curr_point not in polygon.perimeter_points:
                        perimeter += calc_dist(curr_point, prev_point)
                else:
                    curr_point = Point(curr_point.x, point_min.y, None, curr_point.next_p)
                    if curr_point not in polygon.perimeter_points:
                        perimeter += calc_dist(curr_point, prev_point)
        else:  # is smaller, need go forward thru red line
            if curr_point.y == point_max.y:
                curr_point = Point(curr_point.x, point_max.y, None, curr_point.next_p)
                if curr_point not in polygon.perimeter_points:
                    perimeter += calc_dist(curr_point, prev_point)
            elif curr_point.x == point_max.x:
                curr_point = Point(curr_point.y, point_max.x, None, curr_point.next_p)
                if curr_point not in polygon.perimeter_points:
                    perimeter += calc_dist(curr_point, prev_point)
            else:
                curr_point = Point(curr_point.x, point_max.y, None, curr_point.next_p)
                if curr_point not in polygon.perimeter_points:
                    perimeter += calc_dist(curr_point, prev_point)

        polygon.perimeter_points.append(curr_point)
        prev_point = copy.copy(curr_point)
        curr_point = curr_point.next_p
        checked_points += 1

    polygon.perimeter = perimeter
    print("[{}] Kernel perimeter: {}".format(polygon.name, perimeter))
