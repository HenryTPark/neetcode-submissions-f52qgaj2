class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]

        for bits in range(1, n + 1):
            # dp[bits] = dp[bits >> 1] + (bits & 1)
            dp.append(dp[bits >> 1] + (bits & 1))


        return dp
        