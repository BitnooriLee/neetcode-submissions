class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        XOR = len(nums)
        for i in range(len(nums)):
            XOR ^=i^nums[i]
        return XOR

