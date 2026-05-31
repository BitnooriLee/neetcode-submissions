class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        h = []
        q_sort = []
        res = [-1] * len(queries)
        for i,q in enumerate(queries):
            q_sort.append((q,i))
        q_sort.sort(key = lambda x:x[0])

        j = 0 
        for q,i in q_sort:
            while(j < len(intervals) and intervals[j][0]<=q ):
                l,r = intervals[j]
                heapq.heappush(h,(r-l+1, r))
                j += 1
            while(h and h[0][1]< q):
                heapq.heappop(h)
            if h:
                res[i] = h[0][0] 

        return res
            

        