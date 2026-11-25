class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for stone in stones:
            heapq.heappush(h, -stone)

        while (len(h) > 1):
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            if s1 > s2:
                heapq.heappush(h, s2-s1)

        return -h[0] if h else 0 