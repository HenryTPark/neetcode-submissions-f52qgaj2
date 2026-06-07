class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        map out char to next possible chars
        
        topologically sort out the order of alphabets
        '''
        indegree = {c: 0 for word in words for c in word}
        char_to_next = defaultdict(set)

        for i in range(len(words) - 1):
            word = words[i]
            next_word = words[i + 1]

            min_len = min(len(word), len(next_word))

            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ''

            for j in range(min_len):
                if word[j] != next_word[j]:
                    if next_word[j] not in char_to_next[word[j]]:
                        indegree[next_word[j]] += 1
                        char_to_next[word[j]].add(next_word[j])
                    break

        res = []
        print('indegree', indegree)
        queue = deque([char for char in indegree if indegree[char] == 0])

        while queue:
            char = queue.popleft()

            res.append(char)

            for next_char in char_to_next[char]:
                indegree[next_char] -= 1

                if indegree[next_char] == 0:
                    queue.append(next_char)

        return ''.join(res) if len(res) == len(indegree) else ''

        

            


        
        
        