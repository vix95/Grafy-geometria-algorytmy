class Tree:
    def __init__(self):
        self.tree = []
        self.points = None
        self.crossed_qty = 0

    def find_end_of_segment(self, index):
        for i, point in enumerate(self.points):
            if not point.is_start and point.segment_id == index:
                return i

        return None

    @staticmethod
    def is_VERTICAL_crossed(current_point, segment):
        return segment.start.x <= current_point.x <= segment.end.x

    @staticmethod
    def is_HORIZONTAL_crossed(current_point, vertical_end, segment):
        return current_point.y >= segment.start.y >= vertical_end.y

    def get_crossed(self, current_point, vertical_end):
        crossed = []
        for segment in self.tree:
            if (self.is_VERTICAL_crossed(current_point, segment)
                    and self.is_HORIZONTAL_crossed(current_point, vertical_end, segment)):
                crossed.append(segment)
                self.crossed_qty += 1

        return False if len(crossed) == 0 else crossed
