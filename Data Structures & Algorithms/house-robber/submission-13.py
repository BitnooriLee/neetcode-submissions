class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        mx = [0] * (len(nums))
        mx[0] = nums[0]
        mx[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            mx[i] = max(mx[i-1], nums[i]+mx[i-2])

        return mx[len(nums)-1]
        