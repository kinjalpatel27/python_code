class Node:
    def __init__(self, name):
        self.name = name
        self.incoming = []
        self.outgoing = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = Node(node)

    def add_edge(self, dependency):
        from_node, to_node = dependency
        assert to_node in list(self.nodes.keys())
        assert from_node in list(self.nodes.keys())
        self.nodes[to_node].incoming.append(self.nodes[from_node])
        self.nodes[from_node].outgoing.append(self.nodes[to_node])

    def remove_edge(self, dependency):
        from_node, to_node = dependency
        assert to_node in list(self.nodes.keys())
        assert from_node in list(self.nodes.keys())
        if self.nodes[from_node] in self.nodes[to_node].incoming:
            self.nodes[to_node].incoming.remove(self.nodes[from_node])
        if self.nodes[to_node] in self.nodes[from_node].outgoing:
            self.nodes[from_node].outgoing.remove(self.nodes[to_node])


def find_project_order(projects, dependencies):
    graph = Graph()

    # time: P
    for proj in projects:
        graph.add_node(proj)

    # time: D
    for dependency in dependencies:
        graph.add_edge(dependency)

    queue = []
    output = []
    # time: P
    for node_key in graph.nodes.keys():
        node = graph.nodes[node_key]
        if len(node.incoming) == 0:
            output.append(node.name)
            if len(node.outgoing) > 0:
                queue.append(node)
    # time: D
    while len(queue) > 0:
        proj = queue.pop(0)
        while len(proj.outgoing) > 0:
            node = proj.outgoing[0]
            graph.remove_edge((proj.name, node.name))
            if len(node.incoming) == 0:
                output.append(node.name)
                if len(node.outgoing) > 0:
                    queue.append(node)
    return output


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
output = find_project_order(projects, dependencies)
print("Output project sequeunce: ", output)

projects = ["a", "b", "c", "d", "e", "f", "g"]
dependencies = [
    ("c", "a"),
    ("f", "c"),
    ("a", "e"),
    ("b", "a"),
    ("d", "g"),
    ("f", "a"),
    ("b", "e"),
    ("f", "b"),
]
output = find_project_order(projects, dependencies)
print("Output project sequeunce: ", output)
