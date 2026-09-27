# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return False

        fast, slow = head, head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            
            slow = slow.next

            if slow == fast:
                return True
        
        return False
        