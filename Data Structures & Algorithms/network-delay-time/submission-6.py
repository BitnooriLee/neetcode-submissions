class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for s,d,t in times:
            adj[s].append((t,d))
  
        h = [(0,k)] 
        visited = set()
        total = 0 

        while h:
            time, cur = heapq.heappop(h)
            if cur in visited:
                continue
            visited.add(cur)
            total = max(total,time)
            for nt, nxt in adj[cur]:
                if nxt not in visited:
                    heapq.heappush(h, (time + nt, nxt))

        return total if len(visited) == n else -1
                    
                

        