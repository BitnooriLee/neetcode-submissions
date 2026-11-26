class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        have = []
        output = []
        for i in range(k):
            heapq.heappush(have, (-nums[i],i))
        
        for r in range(k-1,len(nums)): # l = r-k+1
            while (have and have[0][1] < r-k+1):
                heapq.heappop(have)
            heapq.heappush(have, (-nums[r],r))
            output.append(-have[0][0])




        return output