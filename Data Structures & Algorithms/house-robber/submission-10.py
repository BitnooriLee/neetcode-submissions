class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])
        for i in range(2,len(nums)):
            cur = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = cur
      
        return prev1