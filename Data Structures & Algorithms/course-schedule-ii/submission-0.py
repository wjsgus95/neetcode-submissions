from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topology = defaultdict(set)
        for i, j in prerequisites:
            topology[i].add(j)
        
        ans = []
        visited = set()
        dependents = set()
        def backtrack(course: int) -> bool:
            if course in dependents:
                return False

            if course in visited:
                return True

            for prereq in topology[course]:
                if prereq in visited:
                    continue

                dependents.add(course)
                if not backtrack(prereq):
                    return False
                dependents.remove(course)

            visited.add(course)
            ans.append(course)
            return True
                   
        for i in range(numCourses):
            if not backtrack(i):
                return []
        
        return ans