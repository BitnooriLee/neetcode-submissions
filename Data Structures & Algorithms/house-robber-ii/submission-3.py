class Solution:
    def rob(self, nums: List[int]) -> int:
        def find_max(nums):
            prev1, prev2 = 0,0
            for n in nums:
                cur = max(prev1, prev2+n)
                prev2 = prev1
                prev1 = cur
            return prev1

        if len(nums) == 1:
            return nums[0]
        case1 = find_max(nums[1:])
        case2 = find_max(nums[:-1])

        return max(case1, case2) 

        