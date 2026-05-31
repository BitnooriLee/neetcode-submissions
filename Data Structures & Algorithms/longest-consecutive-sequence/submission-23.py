class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0 

        for n in nums:
            if n-1 not in nums:
                cnt = 0 
                while(n in num_set):
                    cnt += 1 
                    n += 1 
                res = max(res, cnt)

        return res


        