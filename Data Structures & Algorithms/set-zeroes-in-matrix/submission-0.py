class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(MN) Time | O(1) Space
        is_first_row_zero = False
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        is_first_row_zero = True
                        matrix[0][c] = 0
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        is_first_col_zero = matrix[0][0] == 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if is_first_col_zero:
            for r in range(m):
                matrix[r][0] = 0

        if is_first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
