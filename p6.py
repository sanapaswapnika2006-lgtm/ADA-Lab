
from typing import List
from dataclasses import dataclass
import heapq


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Edge] = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        edge = Edge(u, v, weight)
        self.edges.append(edge)

        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    # Find the representative of a set
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    # Union two sets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x == root_y:
            return False

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    def kruskal_mst(self) -> List[Edge]:
        result = []
        parent = list(range(self.V))
        rank = [0] * self.V

        sorted_edges = sorted(self.edges, key=lambda e: e.weight)

        for edge in sorted_edges:
            if self.union(parent, rank, edge.u, edge.v):
                result.append(edge)

            if len(result) == self.V - 1:
                break

        if self.V > 0 and len(result) != self.V - 1:
            raise ValueError("Graph is disconnected; MST does not exist")

        return result

    def prim_mst(self) -> List[Edge]:
        if self.V == 0:
            return []

        visited = [False] * self.V
        result = []

        # (weight, source, destination)
        min_heap = [(0, -1, 0)]

        while min_heap and len(result) < self.V - 1:
            weight, u, v = heapq.heappop(min_heap)

            if visited[v]:
                continue

            visited[v] = True

            if u != -1:
                result.append(Edge(u, v, weight))

            for next_weight, next_v in self.adj[v]:
                if not visited[next_v]:
                    heapq.heappush(
                        min_heap, (next_weight, v, next_v)
                    )

        if len(result) != self.V - 1:
            raise ValueError("Graph is disconnected; MST does not exist")

        return result


# Example usage
g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:")
for edge in g.kruskal_mst():
    print(f"{edge.u} -- {edge.v} : {edge.weight}")

print("\nPrim MST:")
for edge in g.prim_mst():
    print(f"{edge.u} -- {edge.v} : {edge.weight}")
