class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for bit in range(n + 1):
            result[bit] = result[bit >> 1] + (bit & 1)

        return result
        