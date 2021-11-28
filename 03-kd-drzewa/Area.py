"""
    Klasa Area, definiuje obszar poddrzew i szukanego zakresu
"""


class Area:
    def __init__(self, points):
        self.min = points[0]
        self.max = points[1]

    @property
    def get_area_min(self):
        return self.min.x, self.min.y

    @property
    def get_area_max(self):
        return self.max.x, self.max.y
