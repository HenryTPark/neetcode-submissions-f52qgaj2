class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def count_pali(left, right):
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1

                left -= 1
                right += 1

            return count

        for i in range(n):
            res += count_pali(i, i)
            res += count_pali(i, i + 1)
        
        return res

        