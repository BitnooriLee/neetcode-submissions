class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * (len(nums)+1)
        cur_max = nums[0]
        res = 0 

        for i in range(l-1,-1,-1):
            for j in range(i+1,l):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


        

        