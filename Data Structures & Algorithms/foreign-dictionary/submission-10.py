from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        res = []

        for i in range(len(words) - 1):
            word, next_word = words[i], words[i + 1]

            min_len = min(len(word), len(next_word))

            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ''

            for j in range(min_len):
                if word[j] != next_word[j]:
                    if next_word[j] not in adj[word[j]]:
                        adj[word[j]].add(next_word[j])
                        indegree[next_word[j]] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])

        while queue:
            char = queue.popleft()

            res.append(char)

            for next_char in adj[char]:
                indegree[next_char] -= 1

                if indegree[next_char] == 0:
                    queue.append(next_char)

        if len(res) < len(indegree):
            return ''

        return ''.join(res)


            
            



            
        