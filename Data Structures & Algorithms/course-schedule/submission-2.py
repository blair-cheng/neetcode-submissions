class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)] # for index0,course 1,2 relies on it
        indegree = [0] * numCourses # index 0 has 0 prerequisiters
        finished = []
        q = collections.deque()

        for course, pre in prerequisites: # [1,0]
            graph[pre].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                
                q.append(course)

        
        while q:
            course = q.popleft()
            finished.append(course)
            
            for courses in graph[course]:
                indegree[courses] -= 1
                if indegree[courses] == 0:
                    q.append(courses)

        return len(finished) == numCourses  




















