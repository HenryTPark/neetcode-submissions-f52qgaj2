class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # set up trie
        trie = {}
        word_key = "$"

        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}

                node = node[char]

            node[word_key] = word

        result = []
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        # backtrack(row, col, parent_node)
        def backtrack(row, col, parent_node):
            char = board[row][col]
            node = parent_node[char]

            # if i reach the end of a word
            if word_key in node:
                # add them to res
                result.append(node[word_key])

                del node[word_key]

            # mark visited
            board[row][col] = "#"

            # explore neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if inbounds(nr, nc) and board[nr][nc] in node:
                    backtrack(nr, nc, node)

            # restore the visited
            board[row][col] = char

        # go through each cell
        for row in range(m):
            for col in range(n):
                if board[row][col] in trie:
                    # backtrack
                    backtrack(row, col, trie)

        # return res
        return result
