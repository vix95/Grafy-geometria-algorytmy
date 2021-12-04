import os
from Supportive import import_file, graphSets
from Graph import Graph


def run_program(edges, name):
    print("FILE {}: \n---".format(name))

    try:
        g = Graph(edges=edges)
        g.build()
        g.print_graph()
        g.visualize()

        E = [tuple(l) for l in g.edges]
        graph = dict([])
        for i in range(len(E)):
            v1, v2 = E[i]

            if (v1 not in graph):
                graph[v1] = []
            if (v2 not in graph):
                graph[v2] = []

            graph[v1].append(v2)
            graph[v2].append(v1)

        maximalIndependentSet = graphSets(graph)

        # Prints the Result
        for i in maximalIndependentSet:
            print(i, end=" ")
        print("\n")

        max_indp_set(g)

    except OSError as e:
        print(e)


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            run_program(import_file(f), name)


if __name__ == '__main__':
    from_files()  # run program based on files in catalog 'input'
