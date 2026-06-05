class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        prev_row = [0] * (n + 1)

        for r in range(1, m + 1):
            curr_row = [0] * (n + 1)

            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    curr_row[c] = prev_row[c - 1] + 1
                else:
                    curr_row[c] = max(curr_row[c - 1], prev_row[c])
                
            prev_row = curr_row

        return prev_row[-1]

            



        
        


        