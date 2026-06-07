class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_number = 0

        for _ in range(32):
            least_significant_bit = n & 1

            reversed_number = (reversed_number << 1) | least_significant_bit

            n >>= 1

        return reversed_number