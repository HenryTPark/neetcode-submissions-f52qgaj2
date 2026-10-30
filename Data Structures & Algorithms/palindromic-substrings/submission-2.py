class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count_pali(left, right):
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count

        result = 0
        
        for i in range(n):
            result += count_pali(i, i)
            result += count_pali(i, i + 1)
        
        return result

        