import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_top():
            if num < self.max_top():
                self.max_push(num)
                num = self.max_pop()
        
        if self.min_top():
            if num > self.min_top():
                self.min_push(num)
                num = self.min_pop()
        
        if len(self.min_heap) < len(self.max_heap):
            self.min_push(num)
        else:
            self.max_push(num)
    
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_top() + self.max_top()) / 2
        else:
            return self.max_top()
       
    def min_push(self, value: int):
        heapq.heappush(self.min_heap, value)
    
    def max_push(self, value: int):
        heapq.heappush(self.max_heap, -value)
    
    def min_pop(self) -> int:
        return heapq.heappop(self.min_heap)
    
    def max_pop(self) -> int:
        return -heapq.heappop(self.max_heap)
    
    def min_top(self) -> int | None:
        return self.min_heap[0] if self.min_heap else None
    
    def max_top(self) -> int | None:
        return -self.max_heap[0] if self.max_heap else None
