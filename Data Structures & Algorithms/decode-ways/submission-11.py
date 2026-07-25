class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        last, second_last = 1, 1
        
        for i in range(1, n):
            current = 0

            if s[i] != '0':
                current += last

            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                current += second_last

            second_last = last
            last = current

        return last


        