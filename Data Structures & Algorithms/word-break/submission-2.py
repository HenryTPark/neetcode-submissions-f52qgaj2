class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string_length = len(s)
        can_build_substring = [False] * (string_length + 1)
        can_build_substring[0] = True

        for end in range(1, string_length + 1):
            for word in wordDict:
                word_length = len(word)
                start = end - word_length

                if start >= 0 and can_build_substring[start] and s[start:end] == word:
                    can_build_substring[end] = True
                    break

        return can_build_substring[string_length]



