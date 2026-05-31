class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]

        res = float("-inf")
        cur = 0

        for n in nums:
            cur = max(n, cur+n)
            res = max(res, cur)

        return res