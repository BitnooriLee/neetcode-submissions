class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = len(nums)

        for i in range(len(nums)):
            cur ^= i^nums[i]
        return cur
            
        
        