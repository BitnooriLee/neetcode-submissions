"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        intervals.sort(key=lambda x:x.start)
        res = 0 
        minh = [intervals[0].end]
        i = 1
        while(i<n):
            while(minh and intervals[i].start >= minh[0]):
                heapq.heappop(minh)
            heapq.heappush(minh, intervals[i].end)
            res = max(res, len(minh))
            i+= 1

        return res
#Big O n^2 아님 nlogn 왜냐면 heap 연산이 최대 n번만 수행됨