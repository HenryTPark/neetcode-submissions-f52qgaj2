class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.end_symbol = '#'
        

    def insert(self, word: str) -> None:
        node = self.trie

        for char in word:
            if char not in node:
                node[char] = {}
            
            node = node[char]

        node[self.end_symbol] = True
        


    def search(self, word: str) -> bool:
        node = self.trie

        for char in word:
            if char not in node:
                return False
            
            node = node[char]

        return self.end_symbol in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        
        for char in prefix:
            if char not in node:
                return False

            node = node[char]

        return True
        
        