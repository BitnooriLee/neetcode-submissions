class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 1:
            return 0 
        l = len(intervals)
        intervals.sort()
        s1,e1 = intervals[0]
        cnt = 0 

        for s2,e2 in intervals[1:]:
            if e1 > s2:
                cnt += 1
                e1 = min(e1, e2)
            else:
                s1,e1 = s2,e2 
        return cnt 
        