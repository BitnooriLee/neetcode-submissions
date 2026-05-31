class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1,-1]
        if len(nums) == 2:
            return [0,1]
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]],i]
            else:
                seen[nums[i]] = i 
        