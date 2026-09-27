from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [0 for _ in range(len(edges) + 1)]

        def find(node: int) -> int:
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1: int, node2: int) -> bool:
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return True
            
            if ranks[root1] > ranks[root2]:
                parents[root2] = root1
                ranks[root1] += 1
            else:
                parents[root1] = root2
                ranks[root2] += 1 
            
            return False
        
        for node1, node2 in edges:
            if union(node1, node2):
                return [node1, node2]
            