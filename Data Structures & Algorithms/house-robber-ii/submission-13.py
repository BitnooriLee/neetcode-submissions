class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        def dp(start,end):
            prev1, prev2 = 0,0
            for i in range(start, end):
                cur = max(prev1, prev2+nums[i])
                prev2 = prev1
                prev1 = cur
            return prev1
            

        return max(dp(0,len(nums)-1), dp(1, len(nums)))