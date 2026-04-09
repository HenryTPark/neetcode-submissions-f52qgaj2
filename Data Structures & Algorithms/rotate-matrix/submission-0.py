class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self._transpose(matrix)
        self._reflect(matrix)

    def _transpose(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def _reflect(self, matrix):
        n = len(matrix)

        for row in range(n):
            for col in range(n // 2):
                opposite_col = n - 1 - col

                matrix[row][col], matrix[row][opposite_col] = (
                    matrix[row][opposite_col],
                    matrix[row][col],
                )
