from typing import List


class Solution:

    def strassen_multiply(self, A: List[List[int]],
                          B: List[List[int]]) -> List[List[int]]:

        n = len(A)

        # Base case: multiplication of 1 x 1 matrices
        if n == 1:
            return [[A[0][0] * B[0][0]]]

        # Find the middle point
        mid = n // 2

        # Divide matrix A into 4 parts
        A11 = [row[:mid] for row in A[:mid]]
        A12 = [row[mid:] for row in A[:mid]]
        A21 = [row[:mid] for row in A[mid:]]
        A22 = [row[mid:] for row in A[mid:]]

        # Divide matrix B into 4 parts
        B11 = [row[:mid] for row in B[:mid]]
        B12 = [row[mid:] for row in B[:mid]]
        B21 = [row[:mid] for row in B[mid:]]
        B22 = [row[mid:] for row in B[mid:]]

        # Seven multiplications used by Strassen's algorithm
        M1 = self.strassen_multiply(
            self.add(A11, A22),
            self.add(B11, B22)
        )

        M2 = self.strassen_multiply(
            self.add(A21, A22),
            B11
        )

        M3 = self.strassen_multiply(
            A11,
            self.subtract(B12, B22)
        )

        M4 = self.strassen_multiply(
            A22,
            self.subtract(B21, B11)
        )

        M5 = self.strassen_multiply(
            self.add(A11, A12),
            B22
        )

        M6 = self.strassen_multiply(
            self.subtract(A21, A11),
            self.add(B11, B12)
        )

        M7 = self.strassen_multiply(
            self.subtract(A12, A22),
            self.add(B21, B22)
        )

        # Calculate the four parts of the result matrix
        C11 = self.add(self.subtract(self.add(M1, M4), M5), M7)
        C12 = self.add(M3, M5)
        C21 = self.add(M2, M4)
        C22 = self.add(self.subtract(self.add(M1, M3), M2), M6)

        # Combine the four parts
        result = []

        for i in range(mid):
            result.append(C11[i] + C12[i])

        for i in range(mid):
            result.append(C21[i] + C22[i])

        return result

    # Matrix addition
    def add(self, A, B):
        return [
            [A[i][j] + B[i][j] for j in range(len(A))]
            for i in range(len(A))
        ]

    # Matrix subtraction
    def subtract(self, A, B):
        return [
            [A[i][j] - B[i][j] for j in range(len(A))]
            for i in range(len(A))
        ]


# Example for testing
obj = Solution()

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(obj.strassen_multiply(A, B))