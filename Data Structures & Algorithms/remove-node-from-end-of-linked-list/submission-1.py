# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        n = length - n + 1

        fake_head = ListNode()
        fake_head.next = head

        prev = fake_head
        node = head
        while n > 1:
            prev = node
            node = node.next
            n -= 1
        
        if node:
            prev.next = node.next
        else:
            prev.next = None

        return fake_head.next
        