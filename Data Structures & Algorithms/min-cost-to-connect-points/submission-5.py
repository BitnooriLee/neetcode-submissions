class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        frontier = [(0,0)] #dis, dix 0에서 시작 
        visit = set()
        cost = 0 
        l = len(points)
        while l != len(visit):
            while frontier[0][1] in visit: #이미 방문한 점은 제외 
                heapq.heappop(frontier)
            
            dis, idx = heapq.heappop(frontier)
            visit.add(idx)
            cost += dis

            for j in range(l):
                if j not in visit:
                    d = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                    heapq.heappush(frontier, (d, j))

        return cost
            
        