from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in seen:
                j = seen[target - nums[i]]
                if i != j:
                    return [i,j] if i<j else [j,i]
            seen[nums[i]] = i 

        return -1 

        
#time O(n) n 
#space O(n) dic 