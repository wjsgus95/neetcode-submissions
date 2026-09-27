import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fake_head = ListNode()
        pointer = fake_head

        heap = []
        for index, head in enumerate(lists):
            heapq.heappush(heap, (head.val, index, head))
        
        while heap:
            val, index, node = heapq.heappop(heap)

            if node.next:
                next_node = node.next
                heapq.heappush(heap, (next_node.val, index, next_node))

            pointer.next = node
            pointer = pointer.next

        return fake_head.next

                