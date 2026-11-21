class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxlen = 0
        for i in range(len(nums)):
            l = 1 
            if nums[i]-1 not in seen:
                while (nums[i]+l in seen):
                    l += 1
                if l > maxlen:
                    maxlen = l
        return maxlen


        