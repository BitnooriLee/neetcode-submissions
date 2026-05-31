class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])
            
            prev = None
            for i in range(start,len(nums)):
                if prev == nums[i]:
                    continue
                path.append(nums[i])
                prev = nums[i]
                backtrack(i+1)
                path.pop()
               
        
        backtrack(0)

        return res
        
        