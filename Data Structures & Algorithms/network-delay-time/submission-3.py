class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))
        minh = [(0,k)] #time, node 
        visit = set()

        total = 0 

        while minh:
            w1,n1 = heapq.heappop(minh)
            if n1 in visit:
                continue
            visit.add(n1)
            total = max(total, w1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minh, ((w1+w2),n2))
        return total if len(visit) == n else -1