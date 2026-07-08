class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n - 1
        result = float('inf')

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = left + (right - left) // 2

            result = min(result, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


        return result
        