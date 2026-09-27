class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            peek_start, peek_end = ans[-1]

            start, end = intervals[i]

            if start <= peek_end:
                ans[-1] = [peek_start, max(end, peek_end)]
            else:
                ans.append([start, end])
        
        return ans