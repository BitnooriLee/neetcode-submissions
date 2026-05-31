class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0 

        intervals.sort()

        pre_s, pre_e = intervals[0]
        res = 0 
        i = 1 
        while(i<n):
            if pre_e > intervals[i][0]:
                if pre_e > intervals[i][1]:
                    pre_e = intervals[i][1]
                    pre_s = intervals[i][0]
                res+= 1 
            else:
                pre_s, pre_e = intervals[i]
            i+= 1
        return res


