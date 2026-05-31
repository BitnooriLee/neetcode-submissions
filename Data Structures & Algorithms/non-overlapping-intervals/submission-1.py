class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 

        s1,e1 = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            #overlap
            if e1 > intervals[i][0]:
                res += 1 
                e1 = min(e1,intervals[i][1])
            else:
                s1 = intervals[i][0]
                e1 = intervals[i][1]

        return res
        