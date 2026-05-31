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
        intervals.sort(key= lambda x:x.start)
        res = 0
        h = [intervals[0].end]

        for i in range(1,len(intervals)):
            while(h and intervals[i].start >= h[0]): #제일 빨리 끝나는것보다 늦게 시작하면, 방 증가 x pop해줌 
                heapq.heappop(h)
            heapq.heappush(h, (intervals[i].end))
            res = max(res, len(h))
        return res



        
        