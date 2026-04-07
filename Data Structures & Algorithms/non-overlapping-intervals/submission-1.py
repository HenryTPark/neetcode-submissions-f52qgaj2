class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # edge case
        if not intervals:
            return 0

        # sort by end times
        intervals.sort(key=lambda x: x[1])

        # removal_count
        removal_count = 0
        # previous_end
        previous_end = intervals[0][1]

        # go thru intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # if overlap
            if previous_end > start:
                removal_count += 1
            # else (no overlap)
            else:
                previous_end = end

        # return removal_count
        return removal_count
