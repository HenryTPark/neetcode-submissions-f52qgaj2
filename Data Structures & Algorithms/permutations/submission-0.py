# O(n*n!) time | O(n*n!) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(array, i, j):
            array[i], array[j] = array[j], array[i]
        
        permutations = []

        def backtrack(index):
            if index == len(nums) - 1:
                return permutations.append(nums[:])
            
            for i in range(index, len(nums)):
                swap(nums, i, index)
                backtrack(index + 1)
                swap(nums, i, index)
        
        backtrack(0)

        return permutations