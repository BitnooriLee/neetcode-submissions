class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(set)
        for s,d,c in flights:
            adj[s].add((d,c))
        minh = [(0,0,src)] # cost, nth, stop
        best = [[math.inf] * (k + 2) for _ in range(n)]
        best[src][0] = 0

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




