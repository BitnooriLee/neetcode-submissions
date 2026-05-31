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
    
        s,e = intervals[0].start,intervals[0].end
        i = 1
        while(i<n):
            ns,ne = intervals[i].start , intervals[i].end
            if e > ns:
                return False
            s,e = ns, ne
            i+=1
        return True
