"""
    - importowanie danych z plików
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


def graphSets(graph):
    # Base Case - Given Graph
    # has no nodes
    if (len(graph) == 0):
        return []

    # Base Case - Given Graph
    # has 1 node
    if (len(graph) == 1):
        return [list(graph.keys())[0]]

    # Select a vertex from the graph
    vCurrent = list(graph.keys())[0]

    # Case 1 - Proceed removing
    # the selected vertex
    # from the Maximal Set
    graph2 = dict(graph)

    # Delete current vertex
    # from the Graph
    del graph2[vCurrent]

    # Recursive call - Gets
    # Maximal Set,
    # assuming current Vertex
    # not selected
    res1 = graphSets(graph2)

    # Case 2 - Proceed considering
    # the selected vertex as part
    # of the Maximal Set

    # Loop through its neighbours
    for v in graph[vCurrent]:

        # Delete neighbor from
        # the current subgraph
        if (v in graph2):
            del graph2[v]

    # This result set contains VFirst,
    # and the result of recursive
    # call assuming neighbors of vFirst
    # are not selected
    res2 = [vCurrent] + graphSets(graph2)

    # Our final result is the one
    # which is bigger, return it
    if (len(res1) > len(res2)):
        return res1
    return res2
