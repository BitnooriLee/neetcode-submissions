"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n <= 1:
            return True
        intervals.sort(key=lambda x:x.start)
        ps,pe = intervals[0].start, intervals[0].end

        for i in range(1, n):
            if pe > intervals[i].start:
                return False
            pe = intervals[i].end 
        return True