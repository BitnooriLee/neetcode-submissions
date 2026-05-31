class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        s1,e1 = intervals[0]
        cnt = 0 
        for i in range(1,len(intervals)):
            s2,e2 = intervals[i]
            #Overlap
            if s2 < e1: 
                cnt += 1 
                e1 = min(e1,e2)
            else:
                s1,e1 = s2,e2

        return cnt
                