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

        intervals.sort(key = lambda x:x.start)

        h = []
        heapq.heappush(h, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= h[0]:
                heapq.heappop(h) 
                heapq.heappush(h, intervals[i].end)
            else:
                heapq.heappush(h, intervals[i].end)

        return len(h)

        