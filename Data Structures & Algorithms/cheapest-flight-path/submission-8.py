class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
     
        adj = defaultdict(list)
        minh = [(0,0,(src))] # cost, nth, stop visit 필요없이 nth 
        best = [[float("inf")]*(k+2) for _ in range(n)]
        best[src][0] = 0 
        for s,d,c in flights:
            adj[s].append((d,c))    

        while minh:
            cost, nth, cur = heapq.heappop(minh)
            if cur == dst:
                return cost
            if nth == k+1:
                continue
            if cost > best[cur][nth]:
                continue
            for nxt, nxtcost in adj[cur]:
                if nxtcost+cost < best[nxt][nth+1]:
                    heapq.heappush(minh, (cost+nxtcost, nth+1, nxt))
        return -1