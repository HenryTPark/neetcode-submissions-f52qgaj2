class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        one, two = 1, 1

        for i in range(1, len(s)):
            curr = 0

            if s[i] != '0':
                curr += one
            
            two_digit_value = int(s[i - 1 : i + 1])

            if 10 <= two_digit_value <= 26:
                curr += two

            two = one
            one = curr

        return one