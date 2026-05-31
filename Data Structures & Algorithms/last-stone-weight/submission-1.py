class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for stone in stones:
            heapq.heappush(hp, -stone)

        while(len(hp)>1):
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            if x != y:
                heapq.heappush(hp, x-y)

        return -hp[0] if hp else 0

        
        