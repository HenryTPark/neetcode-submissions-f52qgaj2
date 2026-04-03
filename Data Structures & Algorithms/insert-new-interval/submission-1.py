class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # O(N) Time | O(N) Space
        merged_intervals = []

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                merged_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                merged_intervals.append(newInterval)

                return merged_intervals + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        merged_intervals.append(newInterval)

        return merged_intervals
