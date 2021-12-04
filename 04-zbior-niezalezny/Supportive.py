"""
    - importowanie danych z plików
    - szukanie niezaleznego setu danych
"""


def import_file(filename):
    edge_list = []

    with open(filename, 'r') as f:
        d = [list(map(int, coord.strip().split(' '))) for coord in f.readlines()]

    for line in d:
        if len(line) == 2:
            edge_list.append(line)
        else:
            print("[{}] Removed value: {}".format(filename, line))

    return edge_list


def independent_set_recursive(node):
    """ Start from root and go recursive """
    i = 0

    if node.is_leaf:
        node.I = 1
        add_I(node, node.I)

    elif node.has_children and node.children_count > i:
        while node.children_count > i:
            independent_set_recursive(node.child[i])
            i += 1

        """ Solution 1 - worse """
        # node.I = max(1 + sum(int(node.I) for node in node.grandchild), sum(int(node.I) for node in node.child))

        """ Solution 2 - better """
        node.I = max(1 + node.I_grandchildren, node.I_children)
        add_I(node, node.I)

    print("Vertex {}: I = {}".format(node.v, node.I))


def add_I(node, I):
    if node.parent:
        node.parent.I_children += I

        if node.parent.parent:
            node.parent.parent.I_grandchildren += I
