import os
from Supportive import import_file, independent_set_recursive
from Graph import Graph


def run_program(edges, name):
    print("FILE {}: \n---".format(name))

    try:
        g = Graph(edges=edges)
        g.build()
        g.print_graph()
        g.visualize()
        independent_set_recursive(g.root)

        """ Solution 1 - worse """
        # g.I = max(1 + sum(int(node.I) for node in g.root.grandchild), sum(int(node.I) for node in g.root.child))

        """ Solution 2 - better """
        g.I = max(1 + g.root.I_grandchildren, g.root.I_children)

        print("Maximum independent set: {}\n".format(g.I))

    except OSError as e:
        print(e)


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            run_program(import_file(f), name)


if __name__ == '__main__':
    from_files()  # run program based on files in catalog 'input'
