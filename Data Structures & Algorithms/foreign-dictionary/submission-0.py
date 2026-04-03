from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        char_to_next = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for i in range(n - 1):
            word = words[i]
            next_word = words[i + 1]

            min_len = min(len(word), len(next_word))

            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ""

            for j in range(min_len):
                if word[j] != next_word[j]:
                    if next_word[j] not in char_to_next[word[j]]:
                        char_to_next[word[j]].add(next_word[j])
                        indegree[next_word[j]] += 1
                    break

        res = []
        queue = deque([c for c in indegree if indegree[c] == 0])

        while queue:
            char = queue.popleft()
            res.append(char)

            for neighbor in char_to_next[char]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) < len(indegree):
            return ""

        return "".join(res)
