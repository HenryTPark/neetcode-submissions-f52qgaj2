'''

'''




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inbounds(row, col) or board[row][col] != 'O':
                return

            board[row][col] = 'T'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            
            if board[m - 1][col] == 'O':
                dfs(m - 1, col)
        
        for row in range(1, m - 1):
            if board[row][0] == 'O':
                dfs(row, 0)
            
            if board[row][n - 1] == 'O':
                dfs(row, n - 1)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        