import heapq

class MedianFinder:
    def __init__(self):
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None:
        # prioritize pushing into upper (min heap)
        if not self.upper or num >= self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        if len(self.lower) > len(self.upper):
            value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, value)
        elif len(self.upper) > len(self.lower) + 1:
            value = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -value)

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        
        return (self.upper[0] - self.lower[0]) / 2
        
        