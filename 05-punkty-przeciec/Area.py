from matplotlib import pyplot as plt
from Point import SimplePoint
from SegmentType import SegmentType


class Area:
    def __init__(self, points, segments):
        self.X_PLOT_SIZE_MIN = 0
        self.X_PLOT_SIZE_MAX = 0
        self.Y_PLOT_SIZE_MIN = 0
        self.Y_PLOT_SIZE_MAX = 0
        self.points = points
        self.segments = segments
        self.set_chart_size()
        self.intersections = []
        self.fig, self.ax = plt.subplots(figsize=(self.X_PLOT_SIZE_MAX + 2, self.Y_PLOT_SIZE_MAX + 2), dpi=100)

    def add_intersection(self, segment, vertical):
        def calc_det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        x_difference = (segment.start.x - segment.end.x, vertical.start.x - vertical.end.x)
        y_difference = (segment.start.y - segment.end.y, vertical.start.y - vertical.end.y)

        div = calc_det(x_difference, y_difference)
        d = (calc_det(a=(segment.start.x, segment.start.y), b=(segment.end.x, segment.end.y)),
             calc_det(a=(vertical.start.x, vertical.start.y), b=(vertical.end.x, vertical.end.y)))

        x = calc_det(d, x_difference) / div
        y = calc_det(d, y_difference) / div

        self.intersections.append(SimplePoint(x=x, y=y))

    def print_intersections(self):
        if len(self.intersections) > 0:
            print("Intersections: ", end="")
            for point in self.intersections:
                print(f"({point.x}, {point.y})", end=", ")

            print("\b\b\n", end="")

        return

    def get_sorted_points(self):
        points = self.points
        points.sort(key=lambda point: (point.x, not point.is_start, point.segment_type, point.y))
        return points

    def set_chart_size(self):
        for point in self.points:
            if point.x < self.X_PLOT_SIZE_MIN:
                self.X_PLOT_SIZE_MIN = point.x

            if point.x > self.X_PLOT_SIZE_MAX:
                self.X_PLOT_SIZE_MAX = point.x

            if point.y < self.Y_PLOT_SIZE_MIN:
                self.Y_PLOT_SIZE_MIN = point.y

            if point.y > self.Y_PLOT_SIZE_MAX:
                self.Y_PLOT_SIZE_MAX = point.y
