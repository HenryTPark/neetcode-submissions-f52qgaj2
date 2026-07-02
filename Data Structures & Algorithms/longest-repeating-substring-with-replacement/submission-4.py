class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        result = 0
        counter = {}

        for right, right_char in enumerate(s):
            counter[right_char] = counter.get(right_char, 0) + 1
            max_freq = max(counter[right_char], max_freq)

            while right - left + 1 - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
                


        
        
        