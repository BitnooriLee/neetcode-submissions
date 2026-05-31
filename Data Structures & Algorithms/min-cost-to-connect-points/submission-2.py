class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #start from 0 
        frontier = [(0,0)] #distance, idx 
        visit = set()
        cost = 0 
        l = len(points)

        while len(visit) != len(points):
            while(frontier[0][1] in visit):
                heapq.heappop(frontier)
            d,i = heapq.heappop(frontier)
            visit.add(i)
            cost += d 
            for j in range(l):
                if j not in visit:
                    dis = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                    heapq.heappush(frontier,(dis,j))
        return cost 
            

        