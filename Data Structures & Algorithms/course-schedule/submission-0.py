from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {c: [] for c in range(numCourses)}
        indegree = {c: 0 for c in range(numCourses)}


        for sink, source in prerequisites:
            adjList[source].append(sink)
            indegree[sink] += 1

        queue = deque([node for node in indegree if indegree[node] == 0])
        courses_taken = len(queue)

        print(courses_taken)

        while queue:
            course = queue.popleft()

            for next_course in adjList[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    courses_taken += 1
                    queue.append(next_course)

        return courses_taken == numCourses


        