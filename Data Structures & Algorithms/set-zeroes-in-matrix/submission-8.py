class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(MN) Time | O(1) Space
        m, n = len(matrix), len(matrix[0])

        zero_first_row = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        zero_first_row = True
                        matrix[0][col] = 0
                    else:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(m):
                matrix[row][0] = 0
            
        if zero_first_row:
            for col in range(n):
                matrix[0][col] = 0
        

        

        
        