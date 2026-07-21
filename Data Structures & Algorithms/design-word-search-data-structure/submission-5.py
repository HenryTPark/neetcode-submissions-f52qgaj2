class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end_symbol = '#'
        

    def addWord(self, word: str) -> None:
        node = self.trie

        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]

        node[self.end_symbol] = True
        

    def search(self, word: str) -> bool:
        return self._search_word(0, word, self.trie)

    def _search_word(self, index, word, node):
        if index == len(word):
            return self.end_symbol in node

        char = word[index]

        if char == '.':
            for key in node:
                if (
                    key != self.end_symbol 
                    and self._search_word(index + 1, word, node[key])
                ):
                    return True

        if char not in node:
            return False

        return self._search_word(index + 1, word, node[char])



        
