class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []

        new_start, new_end = newInterval
        
        new_added = False
        for start, end in intervals:
            if end < new_start:
                merged.append([start, end])
            elif start > new_end:
                if not new_added:
                    merged.append([new_start, new_end])
                    new_added = True
                    
                merged.append([start, end])
            else:
                new_start, new_end = min(start, new_start), max(end, new_end)
            
        if not new_added:
            merged.append([new_start, new_end])
            new_added = True
        
        return merged