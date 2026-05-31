class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pre = nums[0]
        for i in range(1, len(nums)):
            pre = pre^nums[i]
            
        return pre