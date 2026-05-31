import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mineap = []
        for num in nums:
            heapq.heappush(mineap, num)
            if len(mineap) > k:
                heapq.heappop(mineap)
        
        return mineap[0]
            