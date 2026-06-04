class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        two = 1
        one = 1

        for i in range(1, len(s)):
            cur = 0

            if s[i] != '0':
                cur += one

            two_digit_value = int(s[i - 1 : i + 1])
            if 10 <= two_digit_value <= 26:
                cur += two

            two = one
            one = cur

        return one