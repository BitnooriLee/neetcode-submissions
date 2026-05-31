class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = -float("inf")
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                output = max(output, sum(nums[i:j+1]))

        return output
        