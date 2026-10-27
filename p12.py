
from typing import List


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and \
                   dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)

    if len(freq) != n:
        raise ValueError("Keys and frequencies must have equal lengths")

    if any(f < 0 for f in freq):
        raise ValueError("Frequencies cannot be negative")

    if n == 0:
        return 0

    # dp[i][j] = minimum search cost for keys i through j
    dp = [[0] * n for _ in range(n)]

    # Prefix sums allow fast frequency-range calculation
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_freq = prefix[j + 1] - prefix[i]
            dp[i][j] = float('inf')

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total_freq
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# Example 1: Floyd-Warshall
INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

print("Shortest distance matrix:")
for row in floyd_warshall(graph):
    print(row)


# Example 2: Optimal BST
keys = [10, 20, 30]
freq = [34, 8, 50]

print("Minimum Optimal BST cost:", optimal_bst(keys, freq))
