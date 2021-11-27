"""
    Idea
    - parametr d na wejściu do metody budowania drzewa oznaczający głebokość w drzewie; d = 0
    - jesli S zawiera tylko jeden punkt to zwróć liść pamiętający ten punkt
    - jesli d jest parzyste to podziel na dwa zbiory pionową prostą 'l' przechodząca przez medianę współprzędnych 'x'
        z punktów S, gdzie S1 jest na lewo od mediany, a S2 na prawo
    - w przypadku gdy d jest nieparzyste to dziel S na dwa zbiory poziomą prostą 'l' przechodzącą przez medianę
        współrzędnych y punktów z S, gdzie S1 zawiera punkty poniżej lub na prostej, a S2 zawiera punkty powyżej
    - rekurencyjnie wyznacz kd-drzewa T1 dla S1 oraz T2 dla S2 z parametrem 'd + 1'
    - zwróć korzeń 'v' (z prostą l), z T1 jako jego lewym synem, a z T2 jako prawym synem

"""


import functools
from copy import deepcopy
from matplotlib import pyplot as plt
from Area import Area


class Tree:
    def __init__(self, points, plot_max_size):
        self.plot_max_size = plot_max_size
        self.fig, self.ax = plt.subplots(figsize=(plot_max_size, plot_max_size), dpi=100)

        self.points = {
            "all": points,
            "0": sorted(points, key=functools.cmp_to_key(self.compare_by_x)),  # x_sorted
            "1": sorted(points, key=functools.cmp_to_key(self.compare_by_y))  # y_sorted
        }

        self.points["all_sorted"] = [self.points.get("x_sorted"), self.points.get("y_sorted")]
        self.tree = self.build([self.points.get("0"), self.points.get("1")])
        self.set_parents()

    def set_parents(self):
        for node in self.tree.in_order():
            node.assign_parent()

    @staticmethod
    def get_median_point(points, n):
        """ O(n) """
        n_half = n // 2
        return n_half, points[n_half]

    def build(self, points, d=0):
        """ Recursive function - O(n log n) """
        xy = d % 2
        n = len(points[xy])

        if n == 1:
            return TreeNode(points[xy][0], None, None, None, xy, d=d)
        elif n == 0:
            return None

        (ind, median_point) = self.get_median_point(points[xy], n)
        median = median_point.xy[xy]

        xy_2d = 0 if xy == 1 else 1
        del points[xy][ind]
        for i, point in enumerate(points[xy_2d]):
            if point == median_point:
                del points[xy_2d][i]
                break

        (left_x, right_x) = self.divide_points(points[0], xy, median)  # x
        (left_y, right_y) = self.divide_points(points[1], xy, median)  # y

        t1 = self.build((left_x, left_y), d=d + 1)  # left Tree
        t2 = self.build((right_x, right_y), d=d + 1)  # right Tree

        return TreeNode(median_point, median, t1, t2, xy, d=d)

    @staticmethod
    def divide_points(points, xy, median):
        left = []
        right = []
        for i, point in enumerate(points):
            if (xy == 0 and point.get_x() <= median) or (xy == 1 and point.get_y() <= median):
                left.append(point)
            else:
                right.append(point)

        return left, right

    @staticmethod
    def compare_by_x(p1, p2):
        if p1.get_x() < p2.get_x():
            return -1
        elif p1.get_x() > p2.get_x():
            return 1
        else:
            return 0

    @staticmethod
    def compare_by_y(p1, p2):
        if p1.get_y() < p2.get_y():
            return -1
        elif p1.get_y() > p2.get_y():
            return 1
        else:
            return 0

    @staticmethod
    def print_points(points):
        for p in points:
            print(p.get_xy(), end=", ")

        print("\b\b", end="")
        print("")


class TreeNode:
    def __init__(self, point, median, left, right, xy, d):
        self.point = point
        self.median = median
        self.left = left
        self.right = right
        self.xy = xy
        self.d = d
        self.parent = None

    @property
    def is_leaf(self):
        return not (self.left or self.right)

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_left(self):
        return self.parent and self == self.parent.left

    @property
    def is_right(self):
        return self.parent and self == self.parent.right

    def assign_parent(self):
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def in_order(self):

        if not self:
            return

        if self.left:
            for x in self.left.in_order():
                yield x

        yield self

        if self.right:
            for x in self.right.in_order():
                yield x
