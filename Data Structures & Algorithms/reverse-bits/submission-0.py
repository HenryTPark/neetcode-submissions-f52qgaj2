class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            least_significant_bit = n & 1

            res = (res << 1) | least_significant_bit

            n >>= 1


        return res
        