class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(1) Time | O(1) Space
        result = 0

        while n:
            n &= (n - 1)
            result +=1 
        
        return result
        