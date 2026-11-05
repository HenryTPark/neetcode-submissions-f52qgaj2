class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N) Time | O(N) Space
        indices = {}

        for i, n in enumerate(nums):
            comp = target - n

            if comp in indices:
                return [indices[comp], i]
            
            indices[n] = i
        
        return [-1, -1]
        