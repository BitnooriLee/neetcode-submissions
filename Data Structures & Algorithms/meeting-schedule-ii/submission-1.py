"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st = sorted([i.start for i in intervals])
        ed = sorted([i.end for i in intervals])

        res = cnt = 0 
        s = e = 0
        while s < len(intervals):
            if st[s] < ed[e]:
                s += 1 
                cnt += 1 
            else:
                e += 1
                cnt -= 1 
            res = max(res,cnt)

        return res 
        