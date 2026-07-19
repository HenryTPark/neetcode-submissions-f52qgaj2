class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []


        def backtrack(index, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return

            for i in range(index, len(nums)):
                num = nums[i]

                if current_sum + num <= target:
                    path.append(num)
                    backtrack(i, path, current_sum + num)
                    path.pop()
        
        backtrack(0, [], 0)

        return result
            
        