from Segment import Segment


class Node:
    def __init__(self, segment: Segment):
        self.segment = segment
        self.left = None
        self.right = None
        self.key = (segment.start.y, segment.segment_index)
