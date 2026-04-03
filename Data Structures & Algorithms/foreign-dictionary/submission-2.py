from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        char_to_next = defaultdict(set)
        n = len(words)
        indegree = {c:0 for word in words for c in word}
        
        for i in range(n - 1):
            word, next_word = words[i], words[i + 1]
            
            min_len = min(len(word), len(next_word))
            
            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ''

            for j in range(min_len):
                char, next_char = word[j], next_word[j]
                if char != next_char:
                    if next_char not in char_to_next[char]:
                        char_to_next[char].add(next_char)
                        indegree[next_char] += 1
                    break

        res = []
        queue = deque([c for c in indegree if indegree[c] == 0])

        while queue:
            char = queue.popleft()
            res.append(char)

            for next_char in char_to_next[char]:
                indegree[next_char] -= 1

                if indegree[next_char] == 0:
                    queue.append(next_char)

        if len(res) < len(indegree):
            return ''

        return ''.join(res)




                        
        
        