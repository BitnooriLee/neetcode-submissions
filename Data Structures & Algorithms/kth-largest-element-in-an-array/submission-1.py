class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            heapq.heappush(hp, -num)
        for _ in range(k-1):
            heapq.heappop(hp)
        return -hp[0]
        