class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        path = []

        def helper(current, index):
            if current > target:
                return
            if current == target:
                result.append(path[:])
                return
            
            for i in range(index, len(nums)):
                num = nums[i]

                if current + num <= target:
                    path.append(num)
                    helper(current + num, i)
                    path.pop()

        helper(0, 0)

        return result

        


        