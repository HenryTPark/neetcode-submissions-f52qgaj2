class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for word in wordDict:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]

            node["*"] = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for start in range(n):
            if not dp[start]:
                continue

            node = trie

            for end in range(start, n):
                char = s[end]

                if char not in node:
                    break

                node = node[char]

                if "*" in node:
                    dp[end + 1] = True

        return dp[-1]
