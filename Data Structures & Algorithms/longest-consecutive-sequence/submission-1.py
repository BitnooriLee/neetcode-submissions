class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0 
        for num in nums:
            if num-1 not in set_nums: #new sequence
                cur_ln = 1 
                while num+cur_ln in set_nums:
                    cur_ln += 1
                res = max(res, cur_ln)

        return res

        
        