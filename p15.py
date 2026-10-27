
from typing import List


class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.V = len(graph)

    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.V

        def is_safe(vertex, color):
            for neighbor in range(self.V):
                if (self.graph[vertex][neighbor] != 0 and
                        colors[neighbor] == color):
                    return False
            return True

        def backtrack(vertex):
            if vertex == self.V:
                return True

            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors
        return []

    def hamiltonian_cycle(self) -> List[int]:
        path = [0] * self.V
        path[0] = 0

        def is_safe(vertex, pos):
            if self.graph[path[pos - 1]][vertex] == 0:
                return False

            if vertex in path[:pos]:
                return False

            return True

        def backtrack(pos):
            if pos == self.V:
                return self.graph[path[pos - 1]][path[0]] != 0

            for vertex in range(1, self.V):
                if is_safe(vertex, pos):
                    path[pos] = vertex

                    if backtrack(pos + 1):
                        return True

                    path[pos] = 0

            return False

        if self.V == 0:
            return []

        if backtrack(1):
            return path + [path[0]]

        return []


# Example usage
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

gb = GraphBacktracker(graph)

print("Graph Coloring:", gb.graph_coloring(3))
print("Hamiltonian Cycle:", gb.hamiltonian_cycle())
