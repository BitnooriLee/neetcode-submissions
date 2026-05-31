class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0 
        cur_len = 0
        for num in nums:
            if (num - 1) not in s: #start of seq
                cur_len = 1 
                while (num + cur_len) in s:
                    cur_len+=1 
            longest = max(longest, cur_len)
        return longest

            

            
        