from matplotlib import pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Area:
    def __init__(self, points):
        self.X_PLOT_SIZE = 15
        self.Y_PLOT_SIZE = 7
        self.fig, self.ax = plt.subplots(figsize=(self.X_PLOT_SIZE, self.Y_PLOT_SIZE), dpi=100)
        self.points = points
        self.C_points = []
        self.line = 0  # default value as 0; from left to right
        self.intersections = []

        for pair in self.points:
            self.C_points.append(Point(x=pair[0][0], y=pair[0][1]))
            self.C_points.append(Point(x=pair[1][0], y=pair[1][1]))

    def add_intersection(self, tup):
        self.intersections.append(Point(x=tup[0], y=tup[1]))

    def print_intersections(self):
        if len(self.intersections) > 0:
            print("Intersections: ", end="")
            for point in self.intersections:
                print(f"({point.x}, {point.y})", end=", ")

            print("\b\b\n", end="")

        return

    def met_horizontal_line(self, line):
        return self.line == line[0][0] and self.line == line[1][0]
