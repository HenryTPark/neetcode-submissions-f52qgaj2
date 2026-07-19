class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(M * N * 3 ^ L) Time | O(min(M, N)) Space
        # M: num rows | N: num cols | L: length of word
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            char = board[row][col]

            board[row][col] = '#'

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and board[next_row][next_col] == word[index]
                ):
                    if dfs(next_row, next_col, index + 1):
                        return True
            
            board[row][col] = char
            
            return False

        for row in range(m):
            for col in range(n):
                if (
                    board[row][col] == word[0]
                    and dfs(row, col, 1)
                ):
                    return True
            
        return False


        