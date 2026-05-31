class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i, (x,y) in enumerate(points): 
            heapq.heappush(dis, (-(x*x+y*y),i))
            while len(dis) > k:
                heapq.heappop(dis)
        res = []
        while dis:
            (d, cur) = heapq.heappop(dis)
            res.append(points[cur])
        return res




        