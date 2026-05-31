class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        frontier = [(0,0)] #distance, idx 
        visit = set()
        cost = 0 
  
        while len(points) != len(visit):
            while(frontier[0][1] in visit):
                heapq.heappop(frontier)
            d,i = heapq.heappop(frontier)
            visit.add(i)
            cost += d 
            
            #모든점에서 탐색, 방문한것 제외
            for j in range(len(points)):
                if j not in visit:
                    d = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
                    heapq.heappush(frontier, (d,j))

        return cost
                    