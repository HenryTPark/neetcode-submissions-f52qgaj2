from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.lower = [] # max_heap
        self.upper = [] # min_heap

    def addNum(self, num: int) -> None:
        # Push to lower (max-heap) first, then move the largest of lower to upper
        heappush(self.lower, -num)
        heappush(self.upper, -heappop(self.lower))

        # Maintain size balance: lower can have at most 1 more element than upper
        if len(self.upper) > len(self.lower):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        length = len(self.upper) + len(self.lower)

        if length % 2:
            return float(-self.lower[0])
        else:
            left = -self.lower[0]
            right = self.upper[0]

            return (left + right) / 2