from Point import Point


class Segment:
    def __init__(self, start: Point, end: Point, segment_index: int):
        self.start = start
        self.end = end
        self.segment_index = segment_index
