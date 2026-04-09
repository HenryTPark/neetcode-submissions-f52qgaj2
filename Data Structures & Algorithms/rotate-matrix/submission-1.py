class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def swap(row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row in range(n):
            for col in range(row + 1, n):
                swap(row, col, col, row)

        for row in range(n):
            for col in range(n // 2):
                opposite_col = n - col - 1
                swap(row, col, row, opposite_col)

        
        