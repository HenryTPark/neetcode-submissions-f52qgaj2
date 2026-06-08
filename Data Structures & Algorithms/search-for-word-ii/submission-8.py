class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        found_words = []

        # construct a trie
        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}
                
                node = node[char]

            node['*'] = word

        m, n = len(board), len(board[0])

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col, parent_node):
            char = board[row][col]
            node = parent_node[char]

            if '*' in node:
                found_words.append(node['*'])
                del node['*']

            board[row][col] = '#'

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if inbounds(nr, nc) and board[nr][nc] in node:
                    dfs(nr, nc, node)

            board[row][col] = char

            if not node:
                del parent_node[char]

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return found_words


        

        
        