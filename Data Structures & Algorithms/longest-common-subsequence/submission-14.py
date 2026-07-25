class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # O(MN) Time | O(min(M, N)) Space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        
        prev_row = [0] * (n + 1)

        for row in range(1, m + 1):
            current_row = [0] * (n + 1)

            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    current_row[col] = prev_row[col - 1] + 1
                else:
                    current_row[col] = max(current_row[col - 1], prev_row[col])

            prev_row = current_row

        return prev_row[-1]


        