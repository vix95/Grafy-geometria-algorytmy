class Node:
    def __init__(self, v: int, nxt=None):
        self.v = v
        self.next = nxt
        self.child = []
        self.grandchild = []
        self.parent = None
        self.I = 0

    @property
    def is_leaf(self):
        return len(self.child) == 0

    @property
    def is_root(self):
        return not self.parent

    @property
    def has_children(self):
        return len(self.child) > 0

    @property
    def children_count(self):
        return len(self.child)
