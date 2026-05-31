class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res,cur = 0,0
        nums_set = set(nums)

        for n in nums_set:
            if n-1 not in nums_set:
                cnt = 1 
                while(n+cnt in nums_set):
                    cnt+=1 
                res = max(res,cnt)

        return res 
                
        