class Solution:
    def rob(self, nums: List[int]) -> int:
        last, second_last = 0, 0

        for num in nums:
            temp = max(last, second_last + num)

            second_last = last
            last = temp

        return last


            
        