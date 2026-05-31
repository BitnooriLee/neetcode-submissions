class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = nums[0]

        for i in range(len(nums)):
            if prefix < 0 :
                prefix = 0
            prefix += nums[i] #update prefix 
            res = max(res, prefix)

        return res

        