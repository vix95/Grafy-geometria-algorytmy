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
            O(n^2)
        6. licze najmniejszy dystans miedzy S1 i S2, ustali mi to linie pomocnicze dla S3
            O(1)
        7. dziele punkty z S1 i S2 na S3, ktore wyznaczylem (o ile sie da)
            O(n)
        8. licze dystans dla S3
            O(n)
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

            # calc minimum distance and get points for S1 and S2
            self.s1_min = {"distance": 0.0, "p1": None, "p2": None}
            self.s2_min = {"distance": 0.0, "p1": None, "p2": None}
            self.s3_min = {"distance": 0.0, "p1": None, "p2": None}
            self.get_min_distance(self.s1.get("x"), 1)  # filling s1
            self.get_min_distance(self.s2.get("x"), 2)  # filling s2

            # calc distance for S1 and S2
            self.min_s1_s2_distance = self.set_min_s1_s2_distance()

            # split points by middle S1 and S2
            self.s3 = {
                "s1": self.split_middle_points_by_middle_line(self.s1.get("y")),
                "s2": self.split_middle_points_by_middle_line(self.s2.get("y"))
            }
            self.s3_min["distance"] = self.calc_distance_s3(self.s3.get("s1"), self.s3.get("s2"))

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

    def get_min_distance(self, arr, key):
        min_distance = self.calc_distance(arr[0], arr[1])

        for p1 in arr:
            for p2 in arr:
                if p1 != p2:
                    calc_min = self.calc_distance(p1, p2)
                    if calc_min <= min_distance:
                        min_distance = calc_min

                        if key == 1:  # for S1
                            self.s1_min["distance"] = min_distance
                            self.s1_min["p1"] = p1
                            self.s1_min["p2"] = p2
                        elif key == 2:  # for S2
                            self.s2_min["distance"] = min_distance
                            self.s2_min["p1"] = p1
                            self.s2_min["p2"] = p2

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

    def assign_min_based_on_s3(self, points1, points2):
        is_found = False

        for p1 in points1:
            for p2 in points2:
                dist = self.calc_distance(p1, p2)
                if (p2.get_y() - p1.get_y() <= self.min_s1_s2_distance) and (p1.get_y() - p2.get_y() <= 0):
                    if dist <= self.min_s1_s2_distance:
                        is_found = True
                        self.min_s1_s2_distance = dist
                        self.s3_min["p1"] = p1
                        self.s3_min["p2"] = p2

        return self.min_s1_s2_distance if is_found else -1

    def calc_distance_s3(self, points1, points2):
        min_s3_1 = self.assign_min_based_on_s3(points1, points2)
        min_s3_2 = self.assign_min_based_on_s3(points2, points1)

        if min_s3_1 == -1 and min_s3_2 == -1:
            return -1
        elif min_s3_1 == -1:
            return min_s3_2
        elif min_s3_2 == -1:
            return min_s3_1
        elif min_s3_1 <= min_s3_2:
            return min_s3_1
        else:
            return min_s3_2
