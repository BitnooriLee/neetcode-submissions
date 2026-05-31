class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dis,j])
                adj[j].append([dis,i])

        visit = set()
        minHeap = [(0,0)]
        dis = 0 

        while(len(visit)<n and minHeap):
            d,p = heapq.heappop(minHeap)
            if p in visit:
                continue
            visit.add(p)
            dis += d 
            for nd,np in adj[p]:
                if np not in visit:
                    heapq.heappush(minHeap, (nd,np))
        return dis if len(visit) == n else -1 


        