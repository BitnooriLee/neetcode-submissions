class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in seen:
                j = seen[target - nums[i]]
                return [i,j] if i<j else [j,i]
            seen[nums[i]] = i 

        return -1 

        