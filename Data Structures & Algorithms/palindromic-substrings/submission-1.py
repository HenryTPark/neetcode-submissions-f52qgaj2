class Solution:
    def countSubstrings(self, s: str) -> int:
        # O(N ^ 2) Time | O(1) Space
        n = len(s)
        result = 0

        def count_pali(left, right):
            count = 0

            while (
                left >= 0
                and right < n
                and s[left] == s[right]
            ):
                count += 1

                left -= 1
                right += 1

            return count

        for i in range(n):
            result += count_pali(i, i)
            result += count_pali(i, i + 1)

        return result




        
        
        