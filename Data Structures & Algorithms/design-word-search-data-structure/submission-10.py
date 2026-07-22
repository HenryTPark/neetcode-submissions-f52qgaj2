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
        return self._search_word(word, 0, self.trie)
    
    def _search_word(self, word, index, node):
        if index == len(word):
            return self.end_symbol in node
        
        char = word[index]

        if char == '.':
            for candidate in node:
                if candidate == self.end_symbol:
                    continue

                if self._search_word(word, index + 1, node[candidate]):
                    return True
                
            return False
        
        if char not in node:
            return False
        
        return self._search_word(word, index + 1, node[char])

        
