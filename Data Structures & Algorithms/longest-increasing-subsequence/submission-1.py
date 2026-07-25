from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(NLog(N)) Time | O(1) Space
        subsequence = []

        for num in nums:
            index = bisect_left(subsequence, num)

            if index == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[index] = num

        return len(subsequence)
        