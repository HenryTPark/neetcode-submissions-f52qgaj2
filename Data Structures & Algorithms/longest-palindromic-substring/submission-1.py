class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_left, max_right = 0, 0
        n = len(s)

        def expand_out(left, right):
            while (
                left >= 0
                and right < n
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return (left + 1, right - 1)

        for i in range(n):
            odd_left, odd_right = expand_out(i, i)
            even_left, even_right = expand_out(i, i + 1)

            if max_right - max_left < odd_right - odd_left:
                max_left, max_right = odd_left, odd_right

            if max_right - max_left < even_right - even_left:
                max_left, max_right = even_left, even_right

        return s[max_left : max_right + 1]



        