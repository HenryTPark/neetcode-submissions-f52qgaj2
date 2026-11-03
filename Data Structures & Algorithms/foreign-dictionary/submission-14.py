from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        indegree = {char: 0 for word in words for char in word}

        n = len(words)

        for i in range(n - 1):
            word, next_word = words[i], words[i + 1]
            
            min_len = min(len(word), len(next_word))

            if (
                len(word) > len(next_word)
                and word[:min_len] == next_word[:min_len]
            ):
                return ''

            for j in range(min_len):
                char1, char2 = word[j], next_word[j]

                if char1 != char2:
                    if char2 not in adj[char1]:
                        adj[char1].add(char2)
                        indegree[char2] += 1

                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()

            result.append(char)

            for next_char in adj[char]:
                indegree[next_char] -= 1

                if indegree[next_char] == 0:
                    queue.append(next_char)

        return ''.join(result) if len(result) == len(indegree) else ''

        