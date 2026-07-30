class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(N) Time | O(1) Space
        result = [0] * (n + 1)

        for bit in range(1, n + 1):
            result[bit] = result[bit // 2] + (bit & 1)
        
        return result
        