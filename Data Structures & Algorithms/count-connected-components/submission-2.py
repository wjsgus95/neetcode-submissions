from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        visited = set()
        def bfs(start: int):
            queue = deque()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        ans = 0
        for node in range(n):
            if node not in visited:
                ans += 1
                bfs(node)
        return ans




        