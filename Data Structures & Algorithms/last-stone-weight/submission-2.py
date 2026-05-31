import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxh = []
        for stone in stones:
            heapq.heappush(maxh, -stone)
        
        while(len(maxh) > 1):
            s1 = heapq.heappop(maxh)
            s2 = heapq.heappop(maxh)
            if s1 != s2:
                heapq.heappush(maxh, s1 - s2)

        return -maxh[0] if maxh else 0

        