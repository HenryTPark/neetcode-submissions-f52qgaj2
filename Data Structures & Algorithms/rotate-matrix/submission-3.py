class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose

        # flip across y axis
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(1 + row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(m):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - 1 - col] = matrix[row][n - 1 - col], matrix[row][col]
        
        
        