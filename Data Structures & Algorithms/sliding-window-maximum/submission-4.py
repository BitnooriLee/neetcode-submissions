class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k ==1:
            return nums
        mxh = []
        l = 0 
        output = []
        for i in range(0,k):
            heapq.heappush(mxh, (-nums[i],i))
        for r in range(k-1,len(nums)):
            heapq.heappush(mxh, (-nums[r],r))
            while mxh and (-mxh[0][0] < nums[r] or mxh[0][1]<r-k+1):
                heapq.heappop(mxh)
            output.append(-mxh[0][0])

        return output

#O(nlogn)
#O(n)
        