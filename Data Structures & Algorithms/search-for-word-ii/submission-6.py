class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        found_words = []
        m, n = len(board), len(board[0])

        for word in words:
            node = trie

            for char in word:
                if not char in node:
                    node[char] = {}

                node = node[char]

            node['*'] = word

        def inbounds(r, c):
            return 0 <= r < m and 0 <= c < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c, parent_node):
            char = board[r][c]

            node = parent_node[char]

            if not node:
                del parent_node[char]
                return

            if '*' in node:
                found_words.append(node['*'])

                del node['*']

            board[r][c] = '#'

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbounds(nr, nc) and board[nr][nc] in node:
                    dfs(nr, nc, node)
                
            board[r][c] = char

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return found_words

        

        

        
        
        