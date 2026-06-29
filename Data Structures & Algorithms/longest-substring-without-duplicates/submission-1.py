class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(N) Time | O(1) Space
        last_seen = {}
        result = 0
        left = 0

        for right, right_char in enumerate(s):
            if right_char in last_seen:
                left = max(left, last_seen[right_char] + 1)

            result = max(result, right - left + 1)
            
            last_seen[right_char] = right


        return result
        