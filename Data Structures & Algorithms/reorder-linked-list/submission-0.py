# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        prev = None
        node = mid
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        
        node1 = head
        node2 = prev

        while node1 and node2:
            next1 = node1.next
            next2 = node2.next

            node1.next = node2
            node2.next = next1

            node1 = next1
            node2 = next2
