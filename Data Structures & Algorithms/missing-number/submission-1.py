class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # [0, len(nums)]
        
        for i in range(len(nums)): #nums[i] [0,len(nums)-1]
            res += i - nums[i]

        return res