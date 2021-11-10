from operator import attrgetter

from matplotlib import pyplot as plt


class Point:
    def __init__(self, x, y, prev_p=None, next_p=None):
        self.x = x
        self.y = y
        self.prev_p = prev_p
        self.next_p = next_p
        self.place = None

    def get_xy(self):
        return self.x, self.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Polygon:
    def __init__(self, points, name):
        self.points = points
        self.name = name
        self.max_points = []
        self.min_points = []
        self.max_p = None
        self.min_p = None
        self.is_kernel = None
        self.is_oriented_ok = False
        self.perimeter = 0
        self.perimeter_points = []
        self.fig, self.ax = plt.subplots(figsize=(10, 10), dpi=100)

    def calc_max(self):
        if self.max_points:
            self.max_p = max(self.max_points, key=attrgetter('y'))
        else:
            self.max_p = min(self.points, key=attrgetter('y'))

    def calc_min(self):
        if self.min_points:
            self.min_p = min(self.min_points, key=attrgetter('y'))
        else:
            self.min_p = max(self.points, key=attrgetter('y'))

    def two_points_at_least(self):
        return self.max_p.x != self.min_p.x or self.max_p.y != self.min_p.y
