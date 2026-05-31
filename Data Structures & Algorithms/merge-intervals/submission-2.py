class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        
        s,e = intervals[0]
        res = []
        i = 1 
        while(i<n):
            ns, ne = intervals[i]
            if e < ns:
                res.append([s,e])
                s,e = ns, ne 
                i += 1 
            elif e >= ns:
                s = min(s,ns)
                e = max(e,ne)
                i += 1 
        res.append([s,e])

        return res



        