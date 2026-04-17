class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_first_row_zero = False
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        is_first_row_zero = True
                        matrix[row][col] = 0
                    else:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        is_first_col_zero = matrix[0][0] == 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if is_first_row_zero:
            for col in range(n):
                matrix[0][col] = 0

        if is_first_col_zero:
            for row in range(m):
                matrix[row][0] = 0

        
        
        