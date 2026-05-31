class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        res = []
        intervals.sort()

        ps, pe = intervals[0]
        for s,e in intervals[1:]:
            if pe >= s:
                pe = max(pe,e)
            else:
                res.append([ps,pe])
                ps,pe = s,e 
        res.append([ps,pe])
        return res 




        