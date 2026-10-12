from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        queue = deque()

        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time

                
