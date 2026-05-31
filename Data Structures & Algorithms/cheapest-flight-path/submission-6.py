class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        numf = len(flights)
        best = [[float("inf")]*(k+2) for _ in range(n)]
        dic = {i: [] for i in range(n)}# s: (dst, price)
        for i in range(numf):
            s,d,p = flights[i]
            dic[s].append((d,p))
        
        minHeap=[(0,src,0)]
        best[src][0] = 0
        while(minHeap): # price, d, kth 
            price,point,kth = heapq.heappop(minHeap)
            if kth > k+1:
                continue 
            if price != best[point][kth]: # 가지치기
                continue 
         
            for npoint, nprice in dic[point]:
                if kth+1 <= k+1:
                    if price+nprice < best[npoint][kth+1]:
                        best[npoint][kth+1] = price+nprice
                        heapq.heappush(minHeap, (price+nprice,npoint,kth+1))


        res = float('inf') 
        for price in best[dst]:
            res = min(res,price)
        #res = min(best[dst])

        return res if res != float("inf") else -1 



        