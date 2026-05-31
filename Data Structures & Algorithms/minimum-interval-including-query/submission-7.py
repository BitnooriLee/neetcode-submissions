class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        qs =sorted([(querie, idx) for idx, querie in enumerate(queries)])

        res = [-1]*len(queries)
        h = []
        j = 0 

        for q,i in qs:
            
            while j < len(intervals) and q >= intervals[j][0]:
                s,e = intervals[j]
                heapq.heappush(h, (e-s+1, e))
                j+=1 
            
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            if h:
                res[i] = h[0][0]
            else:
                res[i] = -1

        return res 

        