class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def inbounds(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(r, c, i):
            if i + 1 == len(word):
                return True

            char = word[i]

            board[r][c] = '*'

            for row_shift, col_shift in directions:
                nr, nc = r + row_shift, c + col_shift

                if inbounds(nr, nc) and board[nr][nc] == word[i + 1]:
                    if dfs(nr, nc, i + 1):
                        return True

            board[r][c] = char
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
        