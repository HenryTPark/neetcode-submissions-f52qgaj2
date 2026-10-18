# O(n*n!) time | O(n*n!) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        permutations = []

        def backtrack(index):
            if index == len(nums) - 1:
                return permutations.append(nums[:])
            
            for i in range(index, len(nums)):
                swap(i, index)
                backtrack(index + 1)
                swap(i, index)
        
        backtrack(0)

        return permutations