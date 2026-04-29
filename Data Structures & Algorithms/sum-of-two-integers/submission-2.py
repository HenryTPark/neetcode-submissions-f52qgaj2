class Solution:
    # O(1) Time | O(1) Space
    # Time is bounded by the fixed 32-bit integer limit, so it runs in constant time. Space is also constant.
    def getSum(self, num1: int, num2: int) -> int:
        """
        Calculates the sum of two integers without using standard arithmetic operators.
        Utilizes bitwise XOR for addition and bitwise AND for carrying over bits.
        """
        # 32-bit mask in hexadecimal to simulate 32-bit integer boundaries
        mask = 0xFFFFFFFF

        # Loop until there is no carry left
        while num2 != 0:
            # XOR finds the sum without carry. Apply mask to keep it within 32 bits.
            current_sum = (num1 ^ num2) & mask

            # AND finds the common set bits, shift left by 1 to carry them over.
            current_carry = ((num1 & num2) << 1) & mask

            num1 = current_sum
            num2 = current_carry

        # max_int represents the maximum positive value for a 32-bit signed integer
        max_int = 0x7FFFFFFF

        # If num1 is within the positive range, return it directly.
        # Otherwise, it's a negative number in 32-bit representation;
        # restore it to Python's arbitrary precision negative representation.
        return num1 if num1 <= max_int else ~(num1 ^ mask)