class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N) Time | O(N) Space
        num_to_idx = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_idx:
                return [num_to_idx[complement], i]

            num_to_idx[num] = i

        return [-1, -1]
        