class Graph:

    def __init__(self, graph=None, start=None):
        self.graph = graph

        self.start = start
        self.distances = {node: float('inf') for node in self.graph}
        self.distances[self.start] = 0
        self.previous_nodes = {node: None for node in self.graph}
        self.unvisited = set(self.graph.keys())

    def dijkstra(self):
        while self.unvisited:
            current_node = min(
                (node for node in self.unvisited),
                key=lambda node: self.distances[node]
            )

            self.unvisited.remove(current_node)

            for neighbor, weight in self.graph[current_node].items():
                alternative_route = self.distances[current_node] + weight
                if alternative_route < self.distances[neighbor]:
                    self.distances[neighbor] = alternative_route
                    self.previous_nodes[neighbor] = current_node

        return self.distances, self.previous_nodes
    