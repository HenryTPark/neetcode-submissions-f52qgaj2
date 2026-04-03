class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        output = float('inf')

        while left <= right:
            if nums[left] < nums[right]:
                output = min(output, nums[left])
                break

            mid = (left + right) // 2
            output = min(output, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return output
