from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0

        wordList.append(beginWord)

        adj_list = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]

                adj_list[key].append(word)

        queue = deque([(1, beginWord)])
        visited = set([beginWord])

        while queue:
            dist, word = queue.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]

                for next_word in adj_list[key]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((dist + 1, next_word))

        return 0
        