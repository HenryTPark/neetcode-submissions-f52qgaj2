class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dup = -1
        for num in nums:
            num = abs(num)

            if nums[num - 1] < 0:
                dup = num
                break
            
            nums[num - 1] *= -1

        
        return dup
        