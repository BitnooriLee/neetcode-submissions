class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s,e,t in times:
            adj[s].append((t,e))

        h = [(0,k)] # time, 
        visit = set()

        total = 0 

        while h:
            time, cur = heapq.heappop(h)
            if cur in visit: #heap에 같은 노드가 여러번 들어갈 수 있음 (최단에서 이미 방문한 경우)
                continue
            visit.add(cur)
            total = max(total, time) # 시그널이 동시에 계속 감? 
            for nt, nxt in adj[cur]:
                if nxt not in visit:
                    heapq.heappush(h, ((time+nt),nxt))
        return total if len(visit) == n else -1 
                    
            

        