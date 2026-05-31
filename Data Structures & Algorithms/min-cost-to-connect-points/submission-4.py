class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        frontier = [(0,0)] #dis, idx 

        visit = set()
        cost = 0 
        l = len(points)
        
        while len(visit) != l:
            while(frontier[0][1] in visit): #이미 연결된건 제거 
                heapq.heappop(frontier)
            d,i = heapq.heappop(frontier)
            visit.add(i)
            cost += d

            for j in range(l):
                if j not in visit:
                    dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(frontier, (dis,j))

        return cost