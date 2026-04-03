class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(N) Time | O(1) Space
        char_to_last_seen = {}
        left = 0
        res = 0

        for right, right_char in enumerate(s):
            if right_char in char_to_last_seen:
                left = max(left, char_to_last_seen[right_char] + 1)

            length = right - left + 1
            res = max(res, length)

            char_to_last_seen[right_char] = right

        return res

        
        