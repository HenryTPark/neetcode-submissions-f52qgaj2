class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev_row = [0] * (len(text2) + 1)

        for row in range(1, len(text1) + 1):
            cur_row = [0] * (len(text2) + 1)

            for col in range(1, len(text2) + 1):
                if text1[row - 1] == text2[col - 1]:
                    cur_row[col] = prev_row[col - 1] + 1
                else:
                    cur_row[col] = max(prev_row[col], cur_row[col - 1])
                
            prev_row = cur_row

        return prev_row[-1]
            

        
        