"""
    Klasa Area, definiuje obszar poddrzew i szukanego zakresu
"""


class Area:
    def __init__(self, points):
        self.min = points[0]
        self.max = points[1]
