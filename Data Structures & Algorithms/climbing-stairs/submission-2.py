class Solution:
    def climbStairs(self, n: int) -> int:
        last, second_last = 1, 1

        for _ in range(1, n):
            temp = last + second_last

            second_last = last
            last = temp

        return last

        