class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        res = 1 
        for n in nums:
            cur = 0
            while n-1 in num_set:
                cur += 1
                n +=1 
            res = max(res, cur)


        return res