# coding=utf-8
"""
    Klasa Area zawiera wszystkie funkcje potrzebne do prawidlowej realizacji zadania.
    Cala konfiguracja jest zawarta w __init__. Tworzac obiekt Area, podaje tylko punkty, na podstawie ktorych
    jest wykonywany program.

    Kroki:
        1. laduje punkty do slownika "points[all]"
        2. sortuje zaladowane punkty po wspolrzednej X i Y, zapisuje w slowniku "points[by_x]", "points[by_y]"
            pozwala to na zachowanie odpowieniej kolejnosci
            O(n log n)
        3. na podstawie "points[by_x] wyszukuje srodkowy punkt, ktory podzieli mi obszar na S1 i S2
            O(1)
        4. dziele punkty na S1 i S2 wzgledem "middle point"
            O(n)
        5. licze najmniejszy dystans miedzy kazdym punktem dla S1 i S2
            O(log n)
        6. licze najmniejszy dystans miedzy S1 i S2
            O(1)
"""

from matplotlib import pyplot as plt
import functools
import math


class Area:
    def __init__(self, points):
        self.fig, self.ax = plt.subplots(figsize=(10, 10), dpi=100)

        # list of points
        self.points = {"all": points}

        if len(self.points.get("all")) < 4:
            print("Too few points were given. Enter at least 4.")
        else:
            self.points["by_x"] = sorted(self.points.get("all"), key=functools.cmp_to_key(self.compare_by_x))
            self.points["by_y"] = sorted(self.points.get("all"), key=functools.cmp_to_key(self.compare_by_y))

            # find middle line
            self.middle_index = len(self.points.get("by_x")) / 2
            self.middle_point = self.points.get("by_x")[self.middle_index - 1]

            # split by S1 and S2
            self.s1 = {
                "x": self.points.get("by_x")[:self.middle_index],
                "y": []
            }

            self.s2 = {
                "x": self.points.get("by_x")[self.middle_index:],
                "y": []
            }

            self.split_points_by_middle_line()

            point_1, point_2, min_distance = self.closest_points(self.s1.get("x"), self.s1.get("y"))
            self.s1_min = {"distance": min_distance, "p1": point_1, "p2": point_2}
            point_1, point_2, min_distance = self.closest_points(self.s2.get("x"), self.s2.get("y"))
            self.s2_min = {"distance": min_distance, "p1": point_1, "p2": point_2}

            # calc distance for S1 and S2
            self.min_s1_s2_distance = self.set_min_s1_s2_distance()

    def closest_points(self, by_x, by_y):
        """
            Recursive Function
            O(log n)
        """
        size = len(by_x)

        if size == 1:
            points = [by_x[0], by_y[0]]
            return self.find_closest(points)
        elif size <= 3:
            return self.find_closest(by_x)

        m = size // 2

        middle_point = by_x[m - 1]
        left_y = [p for p in by_y if p.get_x() < middle_point.get_x()]
        right_y = [p for p in by_y if p.get_x() >= middle_point.get_x()]

        (left_p1, left_p2, left_min_distance) = self.closest_points(by_x[:m], left_y)
        (right_p1, right_p2, right_min_distance) = self.closest_points(by_x[m:], right_y)

        if left_min_distance <= right_min_distance:
            results = {"distance": left_min_distance, "p1": left_p1, "p2": left_p2}
        else:
            results = {"distance": right_min_distance, "p1": right_p1, "p2": right_p2}

        # check if one point is on the left side and second is on the right
        (point_1, point_2, p1_p2_min_distance) = self.closest_points_middle(by_x, by_y, results)

        if results.get("distance") <= p1_p2_min_distance:
            return results.get("p1"), results.get("p2"), results.get("distance")
        else:
            return point_1, point_2, p1_p2_min_distance

    def closest_points_middle(self, by_x, by_y, results):
        middle_point = by_x[len(by_x) // 2]

        y = [point for point in by_y
             if point.get_x() <= abs(results.get("distance") - middle_point.get_x())]

        min_distance = results.get("distance")
        points = [results.get("p1"), results.get("p2")]

        for p1 in y:
            for p2 in y:
                if p1 != p2:
                    calc_distance = self.calc_distance(p1, p2)
                    if calc_distance < min_distance:
                        points = p1, p2
                        min_distance = calc_distance

        return points[0], points[1], min_distance

    def find_closest(self, by_x):
        point_1 = by_x[0]
        point_2 = by_x[1]
        min_distance = self.calc_distance(point_1, point_2)

        for p1 in by_x:
            for p2 in by_x:
                if p1 != p2:
                    calc_min = self.calc_distance(p1, p2)
                    if calc_min < min_distance:
                        point_1 = p1
                        point_2 = p2
                        min_distance = calc_min

        return point_1, point_2, min_distance

    @staticmethod
    def compare_by_x(p1, p2):
        if (p1.get_x() == p2.get_x() and p1.get_y() < p2.get_y()) or (p1.get_x() < p2.get_x()):
            return -1
        elif p1.get_x() > p2.get_x():
            return 1
        else:
            return 0

    @staticmethod
    def compare_by_y(p1, p2):
        if (p1.get_y() == p2.get_y() and p1.get_x() < p2.get_x()) or (p1.get_y() < p2.get_y()):
            return -1
        elif p1.get_y() > p2.get_y():
            return 1
        else:
            return 0

    @staticmethod
    def print_points(points):
        for p in points:
            print(p.get_xy()),

        print("")

    @staticmethod
    def compare_points(p1, p2):
        if (p1.get_x() < p2.get_x()) or (p1.get_y() < p2.get_y() and p1.get_x() == p2.get_x()):
            return 1
        elif (p1.get_x() > p2.get_x()) or (p1.get_y() > p2.get_y() and p1.get_x() == p2.get_x()):
            return 0
        else:
            return 1

    def split_points_by_middle_line(self):
        for p in self.points.get("by_y"):
            if self.compare_points(p, self.middle_point):
                self.s1.get("y").append(p)
            else:
                self.s2.get("y").append(p)

    @staticmethod
    def calc_distance(p1, p2):
        return math.sqrt(((p2.get_x() - p1.get_x()) ** 2.0) + ((p2.get_y() - p1.get_y()) ** 2.0))

    def set_min_s1_s2_distance(self):
        if self.s1_min.get("distance") == -1 and self.s2_min.get("distance") == -1:
            return -1
        elif self.s1_min.get("distance") != -1 and self.s2_min.get("distance") != -1:
            return min(self.s1_min.get("distance"), self.s2_min.get("distance"))
        elif self.s1_min.get("distance") == -1:
            return self.s2_min.get("distance")
        elif self.s2_min.get("distance") == -1:
            return self.s1_min.get("distance")

    def split_middle_points_by_middle_line(self, points):
        arr = []
        for p in points:
            diff = abs(p.get_x() - self.middle_point.get_x())
            if diff <= self.min_s1_s2_distance:
                arr.append(p)

        return arr
