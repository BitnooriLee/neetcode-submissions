class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = nums[0]
        for n in nums[1:]:
            cur ^= n
        return cur

        