import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in range(len(points)):
            dis = math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            heapq.heappush(minheap, (dis, i))

        res = []
        while(k > 0 and minheap):
            dis, i = heapq.heappop(minheap)
            k -=1
            res.append(points[i])
        return res
        