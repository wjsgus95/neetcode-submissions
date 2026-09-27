class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.table = dict()

        self.fake_head = ListNode()
        self.fake_tail = ListNode()

        self.fake_head.next = self.fake_tail
        self.fake_tail.prev = self.fake_head

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.remove(node)
            self.add_front(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = value
            self.remove(node)
            self.add_front(node)
        else:
            if len(self.table) == self.capacity:
                self.remove_tail()

            node = ListNode()
            node.key = key
            node.val = value
            self.table[key] = node
            self.add_front(node)

    
    def add_front(self, node: ListNode):
        prev = self.fake_head
        next = self.fake_head.next

        prev.next = node
        node.prev = prev

        next.prev = node
        node.next = next

    def remove(self, node: ListNode):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
            
    def remove_tail(self):
        next = self.fake_tail
        node = self.fake_tail.prev
        prev = node.prev

        prev.next = next
        next.prev = prev

        del self.table[node.key]