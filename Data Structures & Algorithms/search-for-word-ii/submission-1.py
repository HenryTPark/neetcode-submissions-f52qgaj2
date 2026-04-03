class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # O(M * N * 4^L) Time | O(K * L) Space
        # M: rows, N: cols, L: max word length, K: number of words

        # Build Trie
        trie_root = {}
        WORD_KEY = "$"

        for word in words:
            current_node = trie_root
            for char in word:
                if char not in current_node:
                    current_node[char] = {}
                current_node = current_node[char]
            current_node[WORD_KEY] = word

        rows = len(board)
        cols = len(board[0])
        found_words = []

        def backtrack(row_index, col_index, parent_node):
            """
            Performs DFS to find words starting from (row_index, col_index).
            """
            current_char = board[row_index][col_index]
            current_node = parent_node[current_char]

            # Check if a word ends here
            if WORD_KEY in current_node:
                found_words.append(current_node[WORD_KEY])
                # Optimization: Remove the word from Trie to avoid duplicates
                # and redundant searches later.
                del current_node[WORD_KEY]

            # Mark current cell as visited
            board[row_index][col_index] = "#"

            # Explore neighbors: Up, Right, Down, Left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for row_offset, col_offset in directions:
                next_row, next_col = row_index + row_offset, col_index + col_offset

                # Check boundaries and if the next char exists in the current Trie branch
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and board[next_row][next_col] in current_node
                ):
                    backtrack(next_row, next_col, current_node)

            # Backtrack: Restore the cell
            board[row_index][col_index] = current_char

            # Optimization: Prune leaf nodes from Trie to optimize future searches
            if not current_node:
                del parent_node[current_char]

        # Iterate through every cell to start search
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie_root:
                    backtrack(row, col, trie_root)

        return found_words