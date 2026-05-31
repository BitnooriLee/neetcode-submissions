class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = [] 
        hp = []

        for point in points:
            i,j = point 
            heapq.heappush(hp,(i*i + j*j,[i,j]))
        
        for _ in range(k):
            dis, pt = heapq.heappop(hp)
            output.append(pt)

        return output
        