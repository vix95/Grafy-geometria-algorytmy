import math


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.dist = None

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, p):
        return math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
