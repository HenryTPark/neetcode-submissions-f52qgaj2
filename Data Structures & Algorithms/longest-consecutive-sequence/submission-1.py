class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) Time | O(N) Space
        num_set = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in num_set:
                current = num

                while current in num_set:
                    current += 1

                result = max(result, current - num)

        return result
        