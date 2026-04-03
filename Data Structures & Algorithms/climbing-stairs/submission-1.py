class Solution:
    def climbStairs(self, n: int) -> int:
        # O(N) Time | O(1) Space
        if n <= 2:
            return n

        prev, curr = 1, 1

        for i in range(n - 1):
            temp = curr
            
            curr = prev + curr
            prev = temp
        
        return curr
        