"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # O(NLog(N)) Time | O(N) Space
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        end_times = []

        for interval in intervals:
            start, end = interval.start, interval.end

            if not end_times or start < end_times[0]:
                heapq.heappush(end_times, end)
            else:
                heapq.heapreplace(end_times, end)
            
        return len(end_times)
        