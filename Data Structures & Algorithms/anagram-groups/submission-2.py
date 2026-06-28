class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(N) Time | O(N) Space
        anagram_to_words = {}
        ord_a = ord('a')

        for word in strs:
            counter = [0] * 26

            for char in word:
                counter[ord(char) - ord_a] += 1

            key = tuple(counter)

            if key not in anagram_to_words:
                anagram_to_words[key] = []

            anagram_to_words[key].append(word)

        return list(anagram_to_words.values())





        
        
        