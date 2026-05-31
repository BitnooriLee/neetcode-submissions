class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # q,i로 정렬. index보존
        qs = sorted([(q,i) for i,q in enumerate(queries)])
        res = [-1]*len(queries)
        h = []
        j = 0 
        # 모든 s,e intervals에서 q 보다 먼저시작하는걸 heap에 넣고
        for q,i in qs:
            
            while j < len(intervals) and q >= intervals[j][0]:
                s,e = intervals[j]
                heapq.heappush(h, (e-s+1, e))
                j+=1 
            # q 보다 먼저 끝나는걸 pop하고
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            # h 에 남아있으면, 없으면 
            if h:
                res[i] = h[0][0]
        return res

