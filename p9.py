
from typing import List

def knapsack_01(weights: List[int], values: List[int],
                capacity: int) -> int:
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(capacity + 1):
            # Do not select the current item
            dp[i][w] = dp[i - 1][w]

            # Select the item if it fits
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack_01(weights, values, capacity))


from typing import List

def knapsack_01(weights: List[int], values: List[int],
                capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        # Iterate backwards to avoid selecting an item twice
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(
                dp[w],
                value + dp[w - weight]
            )

    return dp[capacity]


# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack_01(weights, values, capacity))
