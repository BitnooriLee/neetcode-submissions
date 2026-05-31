class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x,y = point 
            d = x*x + y*y 
            heapq.heappush(h, (d,(x,y)))
        output = []
        for _ in range(k):
            d, tmp = heapq.heappop(h)
            output.append(tmp)

        return output


        