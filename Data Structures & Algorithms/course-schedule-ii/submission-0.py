class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        needs = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            needs[course] += 1

        ready = deque(
            course
            for course in range(numCourses)
            if needs[course] == 0
        )

        order = []

        while ready:
            course = ready.popleft()
            order.append(course)

            for next_course in graph[course]:
                needs[next_course] -= 1
                if needs[next_course] == 0:
                    ready.append(next_course)

        if len(order) == numCourses:
            return order
        return []