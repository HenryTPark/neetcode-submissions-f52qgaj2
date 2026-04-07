"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.end)

        for i in range(len(intervals) - 1):
            end = intervals[i].end
            next_start = intervals[i + 1].start

            if end > next_start:
                return False

        return True
