from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)

        visited = set()

        def detect_cycle(parent: int, node: int) -> bool:
            for dst in graph[node]:
                if dst == parent:
                    continue
                
                if dst in visited:
                    return True
                else:
                    visited.add(dst)
                    cyclic = detect_cycle(node, dst)
                    if cyclic:
                        return True
            
            return False
        
        visited.add(0)
        is_tree = not detect_cycle(None, 0)

        if len(visited) < n:
            return False
        
        return is_tree
                
