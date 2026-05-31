class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        minh = [(0,0,(src))] # cost, nth, stop
        best = [[float("inf")]*(k+2) for _ in range(n)] # nth 가 k+1 까지 들어가야함 

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
            for nxt, nxt_cost in adj[cur]:
                if nxt_cost + cost < best[nxt][nth+1]:
                    heapq.heappush(minh, (nxt_cost + cost, nth+1, nxt))
        return -1 

            