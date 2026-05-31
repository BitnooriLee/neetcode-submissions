class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = [] #save distance, end value 
        res = {} # dic -> list later 

        #by sorted order of queries, iterate intervals and update minHeap
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1 
            
            # pop if already end 
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1 

        return [res[q] for q in queries]
            



        