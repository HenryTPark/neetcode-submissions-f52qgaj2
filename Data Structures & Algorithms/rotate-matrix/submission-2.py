class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        [
            1 2 3
            4 5 6
            7 8 9
        ]

        '''
        m, n = len(matrix), len(matrix[0])

        def swap(r1, c1, r2, c2):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        # transpose
        for r in range(m):
            for c in range(r + 1, n):
                swap(r, c, c, r)
        
        # flip-y
        for r in range(m):
            for c in range(n // 2):
                swap(r, c, r, n - 1 - c)

        