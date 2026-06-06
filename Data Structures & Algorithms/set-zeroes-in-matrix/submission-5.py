class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        will keep track of which row/col to zero out from the first
        row and column

        matrix[0][0] will indicate whether or not to zero out the first
        col

        to determine zeroing out first row, we'll use a boolean

        go through rows
            go through cols
                if cell is 0
                    if it's first row
                        set zero_first_row to true
                    
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        go through inner cells

        go through first row

        go through first col
        '''
        m, n = len(matrix), len(matrix[0])
        zero_first_row = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        zero_first_row = True
                    else:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(m):
                matrix[row][0] = 0
        if zero_first_row:
            for col in range(n):
                matrix[0][col] = 0



        
        