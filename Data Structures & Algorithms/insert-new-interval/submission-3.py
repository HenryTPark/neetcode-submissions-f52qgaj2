class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged_intervals = []
        new_start, new_end = newInterval

        for i, (start, end) in enumerate(intervals):
            if new_start > end:
                merged_intervals.append([start, end])
            elif start > new_end:
                merged_intervals.append([new_start, new_end])

                return merged_intervals + intervals[i:]
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
            

        merged_intervals.append([new_start, new_end])

        return merged_intervals




