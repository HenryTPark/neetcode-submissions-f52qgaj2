class WordDictionary:
    def __init__(self):
        self.end_key = '*'
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]

        node[self.end_key] = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.root)

    def _search_in_node(self, word, index, node):
        if index == len(word):
            return self.end_key in node

        char = word[index]

        if char == '.':
            for next_char in node:
                if next_char == self.end_key:
                    continue

                if self._search_in_node(word, index + 1, node[next_char]):
                    return True
                
            return False

        if char not in node:
            return False

        return self._search_in_node(word, index + 1, node[char])
