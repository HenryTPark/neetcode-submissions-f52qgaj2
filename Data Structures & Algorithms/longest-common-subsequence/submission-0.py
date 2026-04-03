class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for row in range(1, len1 + 1):
            for col in range(1, len2 + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]

            