from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # O(N * S) Time | O(S) Space
        # N: length of nums array | S: sum of elements in nums array
        
        """
        Bottom-up DP approach.
        Maintains a frequency map of all reachable sums at the current level,
        eliminating the overhead of the recursive call stack.
        """
        dp = defaultdict(int)
        dp[0] = 1
        
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
            
        return dp[target]