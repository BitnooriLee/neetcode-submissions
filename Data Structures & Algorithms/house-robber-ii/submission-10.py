class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def maxi(start, end):
            prev1, prev2 = 0,0
            for i in range(start, end):
                cur = max(prev2+nums[i], prev1)
                prev2 = prev1
                prev1 = cur
            return prev1
            
        return max(maxi(0,len(nums)-1), maxi(1, len(nums)))