class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for row in range(1, m + 1):
            prev_diag = 0

            for col in range(1, n + 1):
                temp = dp[col]

                if text1[row - 1] == text2[col - 1]:
                    dp[col] = prev_diag + 1
                else:
                    dp[col] = max(dp[col - 1], temp)

                prev_diag = temp

        return dp[-1]
        