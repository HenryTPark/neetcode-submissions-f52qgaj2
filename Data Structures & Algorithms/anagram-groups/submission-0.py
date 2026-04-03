from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_words = defaultdict(list)
        ord_a = ord('a')

        for word in strs:
            counter = [0] * 26

            for char in word:
                index = ord(char) - ord_a

                counter[index] += 1 

            anagram = tuple(counter)

            anagram_to_words[anagram].append(word)

        return list(anagram_to_words.values())
            


        