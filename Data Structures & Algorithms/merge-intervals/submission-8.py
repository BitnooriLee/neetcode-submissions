class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = []
        s1,e1 = intervals[0]
        for i in range(1,len(intervals)):
            s2,e2 = intervals[i]
            if s2 <= e1:
                e1 = max(e1,e2)
            else:
                res.append([s1,e1])
                s1 = s2
                e1 = e2
        res.append([s1,e1])

        return res


        