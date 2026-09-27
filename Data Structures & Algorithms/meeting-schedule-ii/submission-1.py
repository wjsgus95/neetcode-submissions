import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda v: v.start)

        heap = []
        for interval in intervals:
            if heap:
                top_end, _ = heap[0]
                if top_end <= interval.start:
                    heapq.heappop(heap)

                heapq.heappush(heap, (interval.end, interval.start))
            else:
                heapq.heappush(heap, (interval.end, interval.start))
        
        return len(heap)
