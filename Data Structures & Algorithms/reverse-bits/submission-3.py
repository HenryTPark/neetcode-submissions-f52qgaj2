class Solution:
    def reverseBits(self, n: int) -> int:
        # O(1) Time | O(1) Space
        res = 0

        for _ in range(32):
            least_sig_bit = n & 1

            res = (res << 1) | least_sig_bit

            n >>= 1

        return res
        