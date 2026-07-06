class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_left, min_right = 0, float('inf')
        
        t_counter = Counter(t)
        
        need = len(t_counter)
        have = 0
        left = 0
        window_counter = {}

        for right, right_char in enumerate(s):
            window_counter[right_char] = window_counter.get(right_char, 0) + 1

            if (
                right_char in t_counter
                and window_counter[right_char] == t_counter[right_char]
            ):
                have += 1

            while have == need:
                if right - left < min_right - min_left:
                    min_left, min_right = left, right

                left_char = s[left]

                window_counter[left_char] -= 1

                if (
                    left_char in t_counter
                    and t_counter[left_char] > window_counter[left_char]
                ):
                    have -= 1

                left += 1

        return s[min_left : min_right + 1] if min_right != float('inf') else ''

        

        