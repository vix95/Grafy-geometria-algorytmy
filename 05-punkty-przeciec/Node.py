from Segment import Segment


class Node:
    def __init__(self, segment: Segment):
        self.segment = segment
        self.left = None
        self.right = None
        self.key = segment.start.y
        self.id = segment.segment_index
        self.height = 1
        self.y_range = [segment.start.y, segment.end.y]

    def update(self, temp):
        self.key = temp.key
        self.segment = temp.segment
        self.id = temp.id
        self.y_range = temp.y_range
