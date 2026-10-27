
from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))
        self.adj[u].append((v, weight))

    def dijkstra(self, src: int) -> List[int]:
        if not 0 <= src < self.V:
            raise ValueError("Invalid source vertex")

        INF = float('inf')
        dist = [INF] * self.V
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, weight in self.adj[u]:
                if weight < 0:
                    raise ValueError(
                        "Dijkstra requires non-negative edge weights"
                    )

                new_dist = dist[u] + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist

    def bellman_ford(self, src: int) -> List[int]:
        if not 0 <= src < self.V:
            raise ValueError("Invalid source vertex")

        INF = float('inf')
        dist = [INF] * self.V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            changed = False

            for u, v, weight in self.edges:
                if dist[u] != INF and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    changed = True

            if not changed:
                break

        # Detect a negative-weight cycle reachable from src
        for u, v, weight in self.edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                raise ValueError("Negative-weight cycle detected")

        return dist


# Example
g = ShortestPath(5)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

src = 0

print("Dijkstra distances:", g.dijkstra(src))
print("Bellman-Ford distances:", g.bellman_ford(src))
