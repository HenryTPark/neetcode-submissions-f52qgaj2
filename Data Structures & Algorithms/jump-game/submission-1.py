class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        min_jump_index = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= min_jump_index:
                min_jump_index = i
        
        return min_jump_index == 0

        