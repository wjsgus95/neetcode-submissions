"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        table = dict()

        new_head = Node(head.val)
        table[head] = new_head

        node = head.next
        new_node = new_head
        while node:
            new_node.next = Node(node.val)
            table[node] = new_node.next

            node = node.next
            new_node = new_node.next
        
        node = head
        new_node = new_head
        while node:
            if node.random:
                new_node.random = table[node.random]

            node = node.next
            new_node = new_node.next
        
        return new_head
        
        