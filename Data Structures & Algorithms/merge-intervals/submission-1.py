class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(NLog(N)) Time | O(N) Space
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1][1] = max(end, result[-1][1])

        return result

        
        