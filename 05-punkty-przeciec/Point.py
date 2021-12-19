from SegmentType import SegmentType


class Point:
    def __init__(self, x: float, y: float, is_start: bool, segment_id: int, segment_type: SegmentType):
        self.x = x
        self.y = y
        self.is_start = is_start
        self.segment_id = segment_id
        self.segment_type = segment_type

    def __str__(self):
        return f"({self.x}, {self.y})"
