class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        def rob_max(nums):
            prev1, prev2 = 0,0
            for i in range(len(nums)):
                cur = max(prev1, prev2+nums[i])
                prev2 = prev1
                prev1 = cur 
            return prev1
                
        return max(rob_max(nums[1:]), rob_max(nums[:len(nums)-1]))
        