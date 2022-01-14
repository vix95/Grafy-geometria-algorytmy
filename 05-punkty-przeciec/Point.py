from SegmentType import SegmentType


class Point:
    def __init__(self, segment_id: int, x: float, y: float, is_start: bool):
        self.segment_id = segment_id
        self.x = x
        self.y = y
        self.is_start = is_start
        self.segment_type = None
        self.segment = None

    def __str__(self):
        return f"({self.x}, {self.y})"


class SimplePoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
