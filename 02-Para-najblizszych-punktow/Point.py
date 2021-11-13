"""
    Klasa Point definiuje punkt na osi X i Y,
    zwraca wspolrzedne. Kazdy punkt to osobny obiekt.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_xy(self):
        return self.x, self.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
