from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(mn) Time | O(min(m, n)) space
        m, n = len(board), len(board[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        visited = set()

        def dfs(r, c, i):
            if i >= len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    inbounds(nr, nc) 
                    and (nr, nc) not in visited 
                    and i + 1 < len(word) 
                    and word[i + 1] == board[nr][nc]
                ):
                    if dfs(nr, nc, i + 1):
                        return True

            visited.remove((r, c))

            return False



            



        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False


'''
[
    ["A","B","C","E"]
    ["S","F","E","S"]
    ["A","D","E","E"]
]
'''
        