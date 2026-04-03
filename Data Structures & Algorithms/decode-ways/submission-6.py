class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        one, two = 1, 1

        for index in range(1, len(s)):
            current = 0

            if s[index] != '0':
                current += one

            two_digit_value = int(s[index - 1 : index + 1])

            if 10 <= two_digit_value <= 26:
                current += two

            two = one
            one = current

        return one
