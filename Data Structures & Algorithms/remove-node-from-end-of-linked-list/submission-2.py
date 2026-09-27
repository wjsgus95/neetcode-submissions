# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake_head = ListNode()
        fake_head.next = head

        prev_slow = None
        fast = fake_head
        slow = fake_head

        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next

            prev_slow = slow
            slow = slow.next
        
        if slow:
            prev_slow.next = slow.next
        else:
            prev_slow.next = None
        
        return fake_head.next