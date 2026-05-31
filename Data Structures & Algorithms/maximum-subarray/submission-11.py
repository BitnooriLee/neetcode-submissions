class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = 0
        res = float("-inf")
        
        for i in range(len(nums)):
            cur_max = max(cur_max+nums[i], nums[i]) 
            res = max(res, cur_max)
        return res