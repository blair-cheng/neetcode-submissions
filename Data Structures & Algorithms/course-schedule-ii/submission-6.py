class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        # eg prerequisites [[1,0],[2,0],[2,1]]
        graph = [[] for _ in range(numCourses)]#[[1,2],[2],[] ] course 0 have 1, 2 relies on it
        indegree = [0]*numCourses # [0,1,2] course 0 has 0 prerequisite
        q = collections.deque() # 0,1,2

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)


        while q:
            course = q.popleft() # 0
            order.append(course) 

            for next_course in graph[course]: # 1,2
                indegree[next_course] -= 1  

                if indegree[next_course] == 0:
                    q.append(next_course)

        return order if len(order) == numCourses else []






        