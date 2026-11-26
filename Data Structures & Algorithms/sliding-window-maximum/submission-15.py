class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        have = []
        output = []
       
        for r in range(len(nums)): # l = r-k+1
            while (have and have[0][1] < r-k+1):
                heapq.heappop(have)
            heapq.heappush(have, (-nums[r],r))
            
            if r >= k-1:
                output.append(-have[0][0])




        return output