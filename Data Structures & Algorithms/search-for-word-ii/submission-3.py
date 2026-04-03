class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        WORD_KEY = "$"

        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}
                
                node = node[char]

            node[WORD_KEY] = word

        m, n = len(board), len(board[0])
        found_words = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(row, col, parent_node):
            char = board[row][col]
            node = parent_node[char]

            if WORD_KEY in node:
                found_words.append(node[WORD_KEY])

                del node[WORD_KEY]

            board[row][col] = '#'

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if inbounds(nr, nc) and board[nr][nc] in node:
                    backtrack(nr, nc, node)

            board[row][col] = char

            if not node:
                del parent_node[char]

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    backtrack(r, c, trie)

        return found_words

            


