class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxh = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(maxh, (-nums[i], i))
            while maxh and maxh[0][1] <= i - k:
                heapq.heappop(maxh)
            if i >= k-1:
                output.append(-maxh[0][0])
        return output


