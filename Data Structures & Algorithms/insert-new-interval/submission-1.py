import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            top_start, top_end = ans[-1]
            start, end = intervals[i]

            if start <= top_end:
                ans[-1] = [top_start, max(end, top_end)]
            else:
                ans.append([start, end])
        
        return ans
