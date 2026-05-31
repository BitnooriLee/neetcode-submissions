class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        prev1 = nums[0]
        prev2 = max(nums[1], nums[0])
        for i in range(2,len(nums)):
            cur = max(prev2, prev1+nums[i])
            prev1 = prev2
            prev2 = cur
      
        return prev2