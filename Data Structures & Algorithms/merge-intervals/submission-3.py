class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals

        intervals.sort()

        s,e = intervals[0]
        i = 1 
        res = []
        while(i<n):
            ns,ne = intervals[i]
            if e < ns:
                res.append([s,e])
                s= ns
                e = ne
            else:
                s = min(s,ns)
                e = max(e,ne)
            i += 1 
        res.append([s,e])

        return res


        