class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.sort()
        n = len(intervals)
        result = []
        new_start, new_end = newInterval

        for i in range(n):
            start, end = intervals[i]

            if new_end < start:
                result.append([new_start, new_end])
                return result + intervals[i:]
            elif new_start > end:
                result.append([start, end])
            else:
                new_start, new_end = min(start, new_start), max(end, new_end)
        
        if not result or result[-1][-1] < new_start:
            result.append([new_start, new_end])

        
        return result
        

            





        