import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, name):
        self.name = name
        self.connection = []


class Graph:
    def __init__(self, vertex=None, directed=False):
        self.nodes = {}
        self.total_nodes = None
        self.directed = directed

        if vertex is not None:
            self.total_nodes = len(vertex)
            for v in vertex:
                self.nodes[v] = Node(v)

    def add_edge(self, node1, node2):
        assert node1.name in list(self.nodes.keys())
        assert node2.name in list(self.nodes.keys())
        if self.directed:
            self.nodes[node1.name].connection.append(node2)
        else:
            self.nodes[node2.name].connection.append(node1)

    def add_vertex(self, vertex):
        self.nodes[vertex] = Node(vertex)
        self.total_nodes += 1


def create_graph_adj_matrix(adj_matrix):
    N = adj_matrix.shape[0]
    vertices = range(N)
    graph = Graph(vertices, directed=True)
    for n1 in range(N):
        for n2 in range(N):
            if adj_matrix[n1, n2]:
                node1 = graph.nodes[n1]
                node2 = graph.nodes[n2]
                graph.add_edge(node1, node2)

    return graph


def find_path(graph, node1, node2):
    queue = []
    queue.append(node1)
    visited = [False] * graph.total_nodes
    while (len(queue)) > 0:
        node = queue.pop(0)
        visited[node.name] = True
        for conn in node.connection:
            if conn == node2:
                return True
            else:
                if not visited[conn.name]:
                    node.visited = True
                    queue.append(conn)
    return False


n_node = 3
adj_matrix = np.random.randint(0, 2, (n_node, n_node))
graph = create_graph_adj_matrix(adj_matrix)

[n1, n2] = np.random.randint(0, n_node, 2)

node1 = graph.nodes[n1]
node2 = graph.nodes[n2]
path_exist = find_path(graph, node1, node2)

nx_graph = nx.DiGraph(adj_matrix)

assert path_exist == nx.has_path(nx_graph, n1, n2)
