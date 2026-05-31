class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        
        intervals.sort()

        ps,pe = intervals[0]
        res = 0 
        for s,e in intervals[1:]:
            if pe <= s:
                ps,pe = s,e
            else:
                pe = min(pe,e)
                res += 1

        return res