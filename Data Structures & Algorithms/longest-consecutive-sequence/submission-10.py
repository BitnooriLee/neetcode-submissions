class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        res = 1
        cur = 1 
        for num in s:
            if num-1 not in s:
                cur = 1
                while(num+cur in s):
                    cur+=1      
            res = max(res, cur)
        return res
