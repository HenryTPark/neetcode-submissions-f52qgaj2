class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s_counter) != len(t_counter):
            return False

        for char in s_counter:
            if s_counter[char] != t_counter.get(char, 0):
                return False

        return True


        
        