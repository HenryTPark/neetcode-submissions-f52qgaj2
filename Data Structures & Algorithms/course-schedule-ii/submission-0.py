from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = {c: 0 for c in range(numCourses)}

        for c, p in prerequisites:
            adj_list[p].append(c)
            indegree[c] += 1

        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()

            result.append(c)

            for nc in adj_list[c]:
                indegree[nc] -= 1

                if indegree[nc] == 0:
                    queue.append(nc)

        return result if len(result) == numCourses else []
            
        
        