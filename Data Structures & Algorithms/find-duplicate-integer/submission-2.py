class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N) Time | O(1) Space
        # N: length of the array

        duplicate = -1
        for num in nums:
            cur = abs(num)
            # If the value at index `cur` is already negative, we've seen `cur` before
            if nums[cur] < 0:
                duplicate = cur
                break
            # Mark the index `cur` as visited by making it negative
            nums[cur] *= -1

        # Optional: Restore array here if needed
        return duplicate
