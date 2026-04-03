from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        s_counter = defaultdict(int)
        t_counter = Counter(t)

        have, need = 0, len(t_counter)
        min_left, min_right = 0, float('inf')

        left = 0

        for right, right_char in enumerate(s):
            s_counter[right_char] += 1

            if s_counter[right_char] == t_counter[right_char]:
                have += 1

            while left <= right and have == need:
                if right - left < min_right - min_left:
                    min_left, min_right = left, right

                left_char = s[left]
                s_counter[left_char] -= 1

                if s_counter[left_char] == t_counter[left_char] - 1:
                    have -= 1

                left += 1

        
        return s[min_left:min_right + 1] if min_right != float('inf') else ''


        
        
        