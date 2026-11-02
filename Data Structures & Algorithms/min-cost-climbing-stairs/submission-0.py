class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        go backwards and step to the lower cost one

        [1 2 3]
        [1 2 i]
        min_costs[i] = min(min_costs[i - 1] + cost[i - 1], min_costs[2] + cost[i - 2])
        
        '''
        n = len(cost)
        min_costs = [0] * (n + 1)

        for i in range(2, n + 1):
            min_costs[i] = min(min_costs[i - 1] + cost[i - 1], min_costs[i - 2] + cost[i - 2])

        return min_costs[-1]

        
        