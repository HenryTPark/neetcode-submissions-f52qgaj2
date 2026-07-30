class Solution:
    def getSum(self, a: int, b: int) -> int:
        # O(1) Time | O(1) Space
        mask = 0xFFFFFFFF

        while b:
            total = (a ^ b) & mask

            carry = ((a & b) << 1) & mask

            a = total
            b = carry

        max_int = 0x7FFFFFFF

        return a if a <= max_int else ~(a ^ mask)
        