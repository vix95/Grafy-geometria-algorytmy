from Node import Node
from Segment import Segment


class Tree:
    def __init__(self):
        self.root = None
        self.points = None
        self.crossed_qty = 0
        self.crossed = []

    def add_node(self, segment: Segment):
        node = Node(segment=segment)
        key = segment.start.y
        p = self.root

        if p is None:
            self.root = node
        elif p is not None:
            while True:
                if key < p.key[0]:
                    if p.left is None:
                        p.left = node
                        break
                    else:
                        p = p.left

                else:
                    if p.right is None:
                        p.right = node
                        break
                    else:
                        p = p.right

    def remove_node(self, root, key):
        if root is None:
            return root

        if key[0] < root.key[0]:
            root.left = self.remove_node(root.left, key)

        elif key[0] > root.key[0]:
            root.right = self.remove_node(root.right, key)

        # so, it's root
        else:
            if root.left is None:
                temp = root.right
                return temp

            elif root.right is None:
                temp = root.left
                return temp

            temp = self.find_left_most_leaf(root.right)
            root.key = temp.key
            root.segment = temp.segment
            root.right = self.remove_node(root.right, temp.key)

        return root

    @staticmethod
    def find_left_most_leaf(node):
        p = node

        while p.left is not None:
            p = p.left

        return p

    def find_end_of_segment(self, index):
        for i, point in enumerate(self.points):
            if not point.is_start and point.segment_id == index:
                return i

        return None

    @staticmethod
    def is_VERTICAL_crossed(current_point, segment):
        return segment.start.x <= current_point.x <= segment.end.x

    @staticmethod
    def is_HORIZONTAL_crossed(vertical_segment, segment):
        return vertical_segment.end.y >= segment.start.y >= vertical_segment.start.y

    def postorder(self, p, crossed, vertical_segment):
        if p is None:
            return

        self.postorder(p.left, crossed, vertical_segment)
        self.postorder(p.right, crossed, vertical_segment)

        if (self.is_VERTICAL_crossed(vertical_segment.start, p.segment)
                and self.is_HORIZONTAL_crossed(vertical_segment, p.segment)):
            self.crossed.append(p.segment)
            self.crossed_qty += 1

    def get_crossed(self, vertical_segment):
        self.crossed = []
        self.postorder(p=self.root, crossed=self.crossed, vertical_segment=vertical_segment)
        return False if len(self.crossed) == 0 else self.crossed
