class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_start, new_end = newInterval
        result = []

        for i in range(n):
            start, end = intervals[i]

            if new_end < start:
                result.append([new_start, new_end])
                return result + intervals[i:]
            elif end < new_start:
                result.append([start, end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
            
        if not result or result[-1][-1] < new_start:
            result.append([new_start, new_end])
        

        return result
        