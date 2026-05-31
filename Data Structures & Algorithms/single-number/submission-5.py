class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for n in nums[1:]:
            a = n^a
        return a
            

        