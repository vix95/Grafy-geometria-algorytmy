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
    elif node.has_children and node.children_count > i:
        while node.children_count > i:
            independent_set_recursive(node.child[i])
            node.I += node.child[i].I
            i += 1

    print("Node {}: I = {}".format(node.v, node.I))

