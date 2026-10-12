import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -1 * heapq.heappop(max_heap)
            second_largest = -1 * heapq.heappop(max_heap)

            if largest != second_largest:
                heapq.heappush(max_heap, -1 * (largest - second_largest))

        return -max_heap[0] if max_heap else 0


        


        