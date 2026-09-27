"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        clones = dict()
        visited = set()
        queue = deque()
        queue.append(node)
        visited.add(node.val)

        while queue:
            n = queue.popleft()

            if not n.val in clones:
                clones[n.val] = Node(val=n.val, neighbors=[])
            clone = clones[n.val]

            for neighbor in n.neighbors:
                if not neighbor.val in clones:
                    clones[neighbor.val] = Node(val=neighbor.val, neighbors=[])
                neighbor_clone = clones[neighbor.val]

                clone.neighbors.append(neighbor_clone)
                
                if not neighbor.val in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)
        
        return clones[node.val]
        