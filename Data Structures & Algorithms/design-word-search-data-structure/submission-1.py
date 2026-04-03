class WordDictionary:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def addWord(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node:
                current_node[char] = {}
            
            current_node = current_node[char]

        current_node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.root)

    def _search_in_node(self, word, index, current_node):
        if index == len(word):
            return self.end_symbol in current_node

        char = word[index]

        if char == '.':
            for child_key in current_node:
                if child_key == self.end_symbol:
                    continue

                if self._search_in_node(word, index + 1, current_node[child_key]):
                    return True

            return False

        if char not in current_node:
            return False

        return self._search_in_node(word, index + 1, current_node[char])


            