class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(Log(N)) Time | O(1) Space
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        