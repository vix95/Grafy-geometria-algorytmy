from Point import Point


class Segment:
    def __init__(self, start: Point, end: Point, segment_index: int):
        self.start = start
        self.end = end
        self.segment_index = segment_index
        self.segment_type = self.start.segment_type
        self.y_range = [start.y, end.y]

    def __str__(self):
        return f"({self.start}, {self.end})"
