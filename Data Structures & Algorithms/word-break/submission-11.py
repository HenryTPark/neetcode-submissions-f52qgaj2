class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(dp)):
            for word in wordDict:
                if i < len(word):
                    continue

                if dp[i - len(word)] and s[i - len(word) : i] == word:
                    dp[i] = True
                    break

        return dp[-1]

                

                    
        