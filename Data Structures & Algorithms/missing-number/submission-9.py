class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = len(nums)

        for i in range(len(nums)):
            cur ^= i^nums[i] # cur n 이고 i 는 0-n-1 
        return cur
            
        
        