class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # [F F F F F F F F F]
        #  0 N E E T C O D E
        #  0 1 2 3 4 5 6 7 8
        # 

        # for word in wordDict:
        #     for i in range(len(word), len(s) + 1):
        #         substring = s[i - len(word) : i + 1]

        #         if substring == word and dp[i - len(word)]:
        #             dp[i] = True

        for i in range(len(dp)):
            for word in wordDict:
                if i < len(word):
                    continue

                if dp[i - len(word)] and s[i - len(word) : i] == word:
                    dp[i] = True


        
        return dp[-1]
        