class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        prefix = 0

        for n in nums:
            if prefix < 0:
                prefix = 0 
            prefix += n 
            maxSub = max(maxSub,prefix)

        return maxSub