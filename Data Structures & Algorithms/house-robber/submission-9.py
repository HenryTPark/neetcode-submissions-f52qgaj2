class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0


        for num in nums:
            two += num

            temp = max(two, one)

            two = one
            one = temp
        
        return one

            


        