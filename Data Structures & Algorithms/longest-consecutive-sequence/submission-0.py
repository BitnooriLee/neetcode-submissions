class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest = 0 

        for number in nums:
            if number-1 not in set_num:
                current_length = 1 
                while number + current_length in set_num:
                    current_length += 1 
                longest = max(longest, current_length)

        return longest 
