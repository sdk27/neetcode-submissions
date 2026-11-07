class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        needs = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            needs[course] += 1

        ready = deque()

        for course in range(numCourses):
            if needs[course] == 0:
                ready.append(course)

        completed = 0

        while ready:
            course = ready.popleft()
            completed += 1

            for next_course in graph[course]:
                needs[next_course] -= 1
                if needs[next_course] == 0:
                    ready.append(next_course)

        return completed == numCourses