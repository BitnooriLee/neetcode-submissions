class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = len(nums) # i... len(nums)하면 0..n까지가 나옴!

        for i in range(len(nums)):
            output^= i^nums[i]

        return output
        