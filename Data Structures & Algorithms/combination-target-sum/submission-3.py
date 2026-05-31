class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = []
        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remain - nums[i])
                path.pop()
            

        backtrack(0, target)

        return res
        
        