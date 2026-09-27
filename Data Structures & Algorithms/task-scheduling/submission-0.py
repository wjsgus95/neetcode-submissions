import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0
        queue = deque()

        counter = Counter(tasks)
        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))
        
        while heap or queue:
            while queue and queue[0][2] < cycle:
                task, count, _ = queue.popleft()
                heapq.heappush(heap, (count, task))
            
            if heap:
                count, task = heapq.heappop(heap)
                if count < -1:
                    queue.append((task, count + 1, cycle + n))

            cycle += 1
        
        return cycle