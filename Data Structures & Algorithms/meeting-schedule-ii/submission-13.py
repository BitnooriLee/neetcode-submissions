"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)

        h = []
        res = 0 
        for i in range(len(intervals)):
            s,e = intervals[i].start, intervals[i].end
            while h and h[0][0] <= s:
                heapq.heappop(h)
            heapq.heappush(h,(e,s))
            res = max(res, len(h))

        return res