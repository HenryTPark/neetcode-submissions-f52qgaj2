class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            current_sum = (a ^ b) & mask
            
            current_carry = ((a & b) << 1) & mask

            a = current_sum
            b = current_carry

        max_int = 0x7FFFFFFF

        return a if a <= max_int else ~(mask ^ a)
        