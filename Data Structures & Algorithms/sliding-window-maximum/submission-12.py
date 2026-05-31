class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
         
        output = []
        max_h = []
        for r in range(len(nums)):
            heapq.heappush(max_h, (-nums[r],r))
            while max_h and max_h[0][1] <= r - k:
                heapq.heappop(max_h)

            if r >= k-1:
                output.append(-max_h[0][0])

        return output


        