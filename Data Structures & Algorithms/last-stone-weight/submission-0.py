class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # - hp
        # pop 
        h = [] 
        for stone in stones:
            heapq.heappush(h, -stone)

        while(len(h) > 1):
            w1 = -heapq.heappop(h)
            w2 = -heapq.heappop(h)
            if w1 == w2:
                continue
            else:
                heapq.heappush(h,w2-w1)
        return -h[0] if h else 0
            
        