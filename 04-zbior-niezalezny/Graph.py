import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import EoN
from Node import Node


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.v_count = np.max(self.edges)
        self.graph = [None] * (self.v_count + 1)
        self.tree = [None] * (self.v_count + 1)
        self.root = None
        self.I = None

    def build(self):
        for edge in self.edges:
            v1 = edge[0]
            v2 = edge[1]
            self.add_edge(v1, v2)

            if not self.tree[v1]:
                node_1 = Node(v=v1)
                node_2 = Node(v=v2)
                node_1.child.append(node_2)
                node_2.parent = node_1
                self.tree[node_1.v] = node_1
                self.tree[node_2.v] = node_2
            else:
                if not self.tree[v2]:
                    node_2 = Node(v=v2)
                    self.tree[node_2.v] = node_2
                else:
                    node_2 = self.tree[v2]

                node_1 = self.tree[v1]
                node_1.child.append(node_2)
                node_2.parent = node_1

            if node_1.parent and node_1.parent.parent and node_1 not in node_1.parent.parent.grandchild:
                node_1.parent.parent.grandchild.append(node_1)
            elif node_2.parent and node_2.parent.parent and node_2 not in node_2.parent.parent.grandchild:
                node_2.parent.parent.grandchild.append(node_2)

            if not self.root:
                self.root = node_1

    def add_edge(self, v1: int, v2: int):
        node = Node(v2, self.graph[v1])
        self.graph[v1] = node

        node = Node(v1, self.graph[v2])
        self.graph[v2] = node

    def print_graph(self):
        for i in range(1, self.v_count + 1):
            print("Vertex {}:".format(i), end="")

            vertex = self.graph[i]
            while vertex:
                print(" -> {}".format(vertex.v), end="")
                vertex = vertex.next

            print("")

        print("\n", end="")

    def visualize(self):
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        pos = EoN.hierarchy_pos(graph, 1)
        nx.draw(graph, pos=pos, with_labels=True, node_color="blue", font_color="white", font_weight="bold")
        plt.show()
