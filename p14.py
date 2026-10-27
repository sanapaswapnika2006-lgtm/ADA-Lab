
from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    board = [["."] * n for _ in range(n)]

    def is_safe(row, col):
        # Check the same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return result


n = int(input("Enter board size: "))
solutions = solveNQueens(n)

print("Total solutions:", len(solutions))
for solution in solutions:
    for row in solution:
        print(row)
    print()
