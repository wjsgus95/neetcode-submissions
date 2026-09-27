"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        START, END = 1, 0
        for it in intervals:
            events.append((it.start, START))
            events.append((it.end, END))
        events.sort()

        stack = 0 
        for timestamp, event_type in events:
            if event_type == START:
                stack += 1
            if event_type == END:
                stack -= 1

            if stack > 1:
                return False
        
        return True