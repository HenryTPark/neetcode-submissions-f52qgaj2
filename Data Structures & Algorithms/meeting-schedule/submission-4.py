"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        end_times = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            if not end_times or start >= -end_times[0]:
                heapq.heappush(end_times, -end)
            else:
                return False

        return True
