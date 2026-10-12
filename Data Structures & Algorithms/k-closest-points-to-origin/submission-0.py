import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            x, y = point

            return math.sqrt(x ** 2 + y ** 2)

        return heapq.nsmallest(k, points, key=lambda p: get_distance(p))
        
        