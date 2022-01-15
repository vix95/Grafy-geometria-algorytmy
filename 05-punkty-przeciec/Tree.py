from Node import Node
from Segment import Segment


class Tree:
    def __init__(self):
        self.root = None
        self.points = None
        self.crossed_qty = 0
        self.crossed = []

    def insert_node(self, root, segment: Segment, key):
        if not root:
            return Node(segment=segment)
        elif key < root.key:
            root.y_range = [min(min(root.y_range), segment.start.y), max(max(root.y_range), segment.end.y)]
            root.left = self.insert_node(root=root.left, segment=segment, key=key)
        else:
            root.y_range = [min(min(root.y_range), segment.start.y), max(max(root.y_range), segment.end.y)]
            root.right = self.insert_node(root=root.right, segment=segment, key=key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # balance tree
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.update(temp=temp)
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance(root)

        # balance the tree
        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    @staticmethod
    def is_HORIZONTAL_crossed(sweep, p):
        return sweep.end.y >= p.y >= sweep.start.y

    @staticmethod
    def is_in_range(sweep, p):
        return ((max(sweep.y_range) >= min(p.y_range) >= min(sweep.y_range))
                or (min(sweep.y_range) <= max(p.y_range) <= max(sweep.y_range)))

    def search(self, p, sweep: Segment):
        """ Search: O(log n) """
        if p is not None:
            in_range = self.is_in_range(sweep=sweep, p=p)

            if in_range:
                horizontal_crossed = self.is_HORIZONTAL_crossed(sweep=sweep, p=p.segment.start)
                if horizontal_crossed:
                    self.crossed.append(p.segment)

                self.search(p=p.left, sweep=sweep)
                self.search(p=p.right, sweep=sweep)
            else:
                print("pass")

    def get_crossed(self, vertical_segment):
        self.crossed = []
        self.search(p=self.root, sweep=vertical_segment)
        self.crossed_qty += len(self.crossed)
        return False if len(self.crossed) == 0 else self.crossed
