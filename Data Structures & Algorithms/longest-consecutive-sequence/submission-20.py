class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
        cur = 0 
        for n in set_nums:
            if n-1 not in set_nums:
                cur = 1 
                while n+cur in set_nums:
                    cur += 1
            res = max(res, cur)

        return res


        