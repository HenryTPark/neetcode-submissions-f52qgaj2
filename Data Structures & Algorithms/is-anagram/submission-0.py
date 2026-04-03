from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s_counter) != len(t_counter):
            return False

        for s_char, s_freq in s_counter.items():
            if s_freq != t_counter[s_char]:
                return False

        return True


        