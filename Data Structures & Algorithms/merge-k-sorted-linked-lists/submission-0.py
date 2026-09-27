# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fake_head = ListNode()
        node = fake_head

        while lists:
            min_index, min_node = min(enumerate(lists), key=lambda v: v[1].val)

            next_node = min_node.next
            if next_node:
                lists[min_index] = next_node
            else:
                lists.pop(min_index)
            
            node.next = min_node
            min_node.next = None
            node = node.next
        
        return fake_head.next