class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        ns, ne = newInterval[0], newInterval[1]
        n = len(intervals)
        i = 0 
        
        while(i<n and intervals[i][1]<ns):
            res.append(intervals[i])
            i += 1

        while(i<n and intervals[i][0]<=ne):
            ns = min(ns,intervals[i][0])
            ne = max(ne,intervals[i][1])
            i += 1
        res.append([ns,ne])

        while(i<n):
            res.append(intervals[i])
            i+= 1
        

        return res