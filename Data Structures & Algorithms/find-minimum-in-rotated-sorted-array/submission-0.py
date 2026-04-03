class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log(N)) Time | O(1) Space
        n = len(nums)
        l, r = 0, n - 1
        res = float('inf')

        while l <= r:
            m = (l + r) // 2

            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                res = min(res, nums[l])
                l = m + 1
            else:
                r = m - 1
        
        return res
        