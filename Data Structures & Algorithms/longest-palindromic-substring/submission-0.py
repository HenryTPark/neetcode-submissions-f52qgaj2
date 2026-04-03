class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def get_longest_pali(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return (left + 1, right - 1)

        max_indices = (0, 0)
        for i in range(n):
            odd_indices = get_longest_pali(i, i)
            even_indices = get_longest_pali(i, i + 1)

            max_indices = max(max_indices, odd_indices, even_indices, key=lambda x: x[1] - x[0])

        max_left, max_right = max_indices
        return s[max_left : max_right + 1]


            
                
        