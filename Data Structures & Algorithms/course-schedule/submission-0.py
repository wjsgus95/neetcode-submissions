from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        influx = defaultdict(int)

        for course, prereq in prerequisites:
            graph[prereq].add(course)
            influx[course] += 1 
        
        queue = deque()
        for course in range(numCourses):
            if influx[course] == 0:
                queue.append(course)
        
        topological = []
        while queue:
            course = queue.popleft()
            topological.append(course)

            for node in graph[course]:
                influx[node] -= 1

                if influx[node] == 0:
                    queue.append(node)
        
        return len(topological) == numCourses