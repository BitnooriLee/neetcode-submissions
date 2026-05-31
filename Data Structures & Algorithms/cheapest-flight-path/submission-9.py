class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list)

        for s,d, c in flights:
            dic[s].append((d,c))
        best = [[float("inf")]*(k+2) for _ in range(n)]
        best[src][0] = 0 

        minh = [(0,0,src)] # cost, nth, stop - visit x, nth로 관리  

        while minh:
            cost, nth, cur = heapq.heappop(minh)
            if cur == dst:
                return cost
            if nth == k+1:
                continue
            if cost > best[cur][nth]:
                continue
            for nxt,nxt_cost in dic[cur]:
                if cost+nxt_cost < best[nxt][nth+1]:
                    heapq.heappush(minh, (cost+nxt_cost, nth+1, nxt))
        return -1 