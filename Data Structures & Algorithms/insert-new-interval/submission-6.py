class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        new_start, new_end = newInterval
        res = []

        # start > new_end
            # append current and everything
        # end > new_end
        # need to merge
        # start end new_start new_end
        # start new_start end new_end
        # new_start start new_end end
        # start

        # start end new_start new_end -> separately attach
        # start new_start end new_end -> merge
        # new_start start new_end end -> merge
        # new_start start end new_end -> merge
        # new_start new_end start end
        

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > new_end:
                res.append([new_start, new_end])
                return res + intervals[i:]
            elif end < new_start:
                res.append([start, end])
            else:
                new_start, new_end = min(start, new_start), max(end, new_end)

        res.append([new_start, new_end])

        return res
        