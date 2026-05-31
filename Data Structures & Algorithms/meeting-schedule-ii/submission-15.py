"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        res = 0
        intervals.sort(key = lambda x:x.start)
        h = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            while(h and intervals[i].start >= h[0]):
                heapq.heappop(h)
            heapq.heappush(h, intervals[i].end)
            res = max(res,len(h))

        return res