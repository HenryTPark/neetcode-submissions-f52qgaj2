class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        previous_row = [0] * (len(text2) + 1)

        for row in range(1, len(text1) + 1):
            current_row = [0] * (len(text2) + 1)

            for col in range(1, len(text2) + 1):
                if text1[row - 1] == text2[col - 1]:
                    current_row[col] = previous_row[col - 1] + 1
                else:
                    current_row[col] = max(previous_row[col], current_row[col - 1])

            previous_row = current_row

        return previous_row[-1]
