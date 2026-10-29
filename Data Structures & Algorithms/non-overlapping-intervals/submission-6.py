class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        have a heap of end_time

        if start >= heap[0]:
            push the end time into heap
        else:
            subtract 1 and 

        sort by end times
        
        keep track of the min end time

        if the current_start < end
            increment 1
            replace min_end_time

        '''
        intervals.sort(key=lambda x: x[1])

        min_end_time = intervals[0][1]
        result = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < min_end_time:
                result += 1

                min_end_time = min(end, min_end_time)
            else:
                min_end_time = end


        return result
        