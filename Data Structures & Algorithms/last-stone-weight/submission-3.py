class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        pq = [-s for s in stones]
        heapq.heapify(pq)

        while len(pq) >= 2:
            w1 = -heapq.heappop(pq)
            w2 = -heapq.heappop(pq)
            if w1 != w2:
                heapq.heappush(pq, w2 - w1)

        return -pq[0] if pq else 0

        
        