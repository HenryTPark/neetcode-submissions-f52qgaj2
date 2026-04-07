class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[1])

        removal_count = 0
        previous_end_time = intervals[0][1]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            if current_start < previous_end_time:
                removal_count += 1
            else:
                previous_end_time = current_end

        return removal_count
