class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0 
        intervals.sort()
        pre_s, pre_e = intervals[0]
        cnt  = 0 
        for s,e in intervals[1:]:
            if pre_e > s:
                cnt+=1 
                pre_e = min(e, pre_e)
            else:
                pre_s,pre_e = s,e 
                
        return cnt

        