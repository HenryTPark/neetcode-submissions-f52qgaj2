from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V + E) Time | O(V + E) Space
        adj_list = defaultdict(list)
        indegree = { course: 0 for course in range(numCourses) }

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        

        queue = deque([course for course in indegree if indegree[course] == 0])

        num_courses_taken = 0

        while queue:
            course = queue.popleft()

            num_courses_taken += 1

            for next_course in adj_list[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return num_courses_taken == numCourses


        