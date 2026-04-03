class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for length in range(2, len(s) + 1):
            single_digit = s[length - 1]

            if single_digit != '0':
                dp[length] += dp[length - 1]
            
            two_digit_value = int(s[length - 2 : length])

            if 10 <= two_digit_value <= 26:
                dp[length] += dp[length - 2]

        return dp[-1]