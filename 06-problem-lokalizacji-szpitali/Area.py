""" Idiot protection not implemented, be carefully :) """
from copy import deepcopy
from matplotlib import pyplot as plt
from Point import Point


class Area:
    def __init__(self, point_list, hospital_count: int = 1):
        self.X_PLOT_SIZE_MIN = 0
        self.X_PLOT_SIZE_MAX = 0
        self.Y_PLOT_SIZE_MIN = 0
        self.Y_PLOT_SIZE_MAX = 0
        self.raw_point_list = point_list
        self.point_list = deepcopy(point_list)
        self.point_count = len(self.raw_point_list)
        self.hospital_count = hospital_count
        self.set_chart_size()
        self.fig, self.ax = plt.subplots(figsize=(5, 5), dpi=200)
        self.opt_dist = 0
        self.hospital_list = []

    def set_chart_size(self):
        self.X_PLOT_SIZE_MIN = (min(self.point_list, key=lambda p: p.x)).x
        self.X_PLOT_SIZE_MAX = (max(self.point_list, key=lambda p: p.x)).x
        self.Y_PLOT_SIZE_MIN = (min(self.point_list, key=lambda p: p.y)).y
        self.Y_PLOT_SIZE_MAX = (max(self.point_list, key=lambda p: p.y)).y

        self.X_PLOT_SIZE_MIN = min(self.X_PLOT_SIZE_MIN, self.Y_PLOT_SIZE_MIN)
        self.Y_PLOT_SIZE_MIN = min(self.X_PLOT_SIZE_MIN, self.Y_PLOT_SIZE_MIN)
        self.X_PLOT_SIZE_MAX = max(self.X_PLOT_SIZE_MAX, self.Y_PLOT_SIZE_MAX)
        self.Y_PLOT_SIZE_MAX = max(self.X_PLOT_SIZE_MAX, self.Y_PLOT_SIZE_MAX)

    def execute(self):
        """
            Algorithm FurthestFirst O(nk)
                1. Pick any point as the hospital localization
                2. Loop j = 1 to k; by longest distance
                3. return S (hospital list)
        """
        self.hospital_list = self.FurthestFirst(point_list=self.point_list, k=self.hospital_count)

        """
            Calculate distance for all cities and get the OPT DISTANCE
            according to last hospital to get the most optimal r
        """
        for city in self.point_list:
            dist = self.calc_opt_dist(hospital=self.hospital_list[-1], city=city, opt_dist=city.dist)
            self.opt_dist = max(dist, self.opt_dist)

    def FurthestFirst(self, point_list, k):
        """
        :param point_list: list of cities
        :param k: count of hospitals
        :return: list of hospitals
        """

        """ Step 1: Pick any point as the hospital localization """
        S = [point_list.pop(0)]

        """ Step 2: Loop i = 1 to k; by longest distance """
        for j in range(1, k):
            long_dist = 0
            p = Point()
            for city in point_list:
                dist = self.calc_opt_dist(hospital=S[j - 1], city=city, opt_dist=city.dist)

                if long_dist < dist:
                    long_dist = dist
                    p = city

            S.append(p)
            point_list.remove(p)

        """ Step 3: return S (hospital list) """
        return S

    @staticmethod
    def calc_opt_dist(hospital: Point, city: Point, opt_dist):
        dist = city.distance(p=hospital)
        opt_dist = dist if not opt_dist else opt_dist
        opt_dist = min(opt_dist, dist)
        city.dist = opt_dist
        return opt_dist
