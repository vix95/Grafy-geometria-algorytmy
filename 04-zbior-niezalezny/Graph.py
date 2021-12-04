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

    def build(self):
        for edge in self.edges:
            self.add_edge(edge[0], edge[1])

    def add_edge(self, v1: int, v2: int):
        node = Node(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node

        node = Node(v1)
        node.next = self.graph[v2]
        self.graph[v2] = node

    def print_graph(self):
        for i in range(1, self.v_count + 1):
            print("Vertex {}:".format(i), end="")

            vertex = self.graph[i]
            while vertex:
                print(" -> {}".format(vertex.v), end="")
                vertex = vertex.next

            print("")

    def visualize(self):
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        pos = EoN.hierarchy_pos(graph, 1)
        nx.draw(graph, pos=pos, with_labels=True, node_color="blue", font_color="white", font_weight="bold")
        plt.show()
