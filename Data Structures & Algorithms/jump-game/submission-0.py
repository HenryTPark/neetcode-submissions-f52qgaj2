class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_reach_index = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            jump_size = nums[i]

            if jump_size + i >= min_reach_index:
                min_reach_index = i

        return min_reach_index == 0
        