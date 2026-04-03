class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        counter = {}
        left = 0
        max_freq = 0

        for right, right_char in enumerate(s):
            counter[right_char] = counter.get(right_char, 0) + 1
            max_freq = max(max_freq, counter[right_char])
            
            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len




         