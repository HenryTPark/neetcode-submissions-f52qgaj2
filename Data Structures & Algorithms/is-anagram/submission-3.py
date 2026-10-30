from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_chars = 0
        counter = [0] * 26
        ord_a = ord('a')

        for char in s:
            index = ord(char) - ord_a

            if counter[index] == 0:
                unique_chars += 1
            
            counter[index] += 1
        
        for char in t:
            index = ord(char) - ord_a


            if counter[index] == 0:
                return False

            counter[index] -= 1

            if counter[index] == 0:
                unique_chars -= 1
        
        return unique_chars == 0
