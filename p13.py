
from typing import List


class TSPSolver:
    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            return 0

        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Distance matrix must be square")

        if n == 1:
            return 0

        INF = float('inf')
        all_visited = (1 << n) - 1

        # dp[mask][u] = minimum cost to start at city 0,
        # visit the cities in mask, and finish at city u.
        dp = [[INF] * n for _ in range(1 << n)]
        dp[1][0] = 0

        for mask in range(1 << n):
            for u in range(n):
                if dp[mask][u] == INF:
                    continue

                for v in range(n):
                    # Visit an unvisited city
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        new_cost = dp[mask][u] + dist_matrix[u][v]

                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            new_cost
                        )

        # Return to the starting city
        answer = min(
            dp[all_visited][u] + dist_matrix[u][0]
            for u in range(1, n)
        )

        return int(answer)


# Example
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()
print("Minimum tour cost:", solver.solve_tsp(dist_matrix))
