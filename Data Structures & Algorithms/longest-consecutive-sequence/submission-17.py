class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0 
        cur = 0
        for n in s: # n in nums로 하면 중복이 발생 
            if n-1 not in s:
                cur = 1 
                while(n+cur in s):
                    cur+=1
            res = max(cur, res)

        return res