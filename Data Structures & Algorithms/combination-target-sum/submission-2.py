class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        def dfs(i, path, remain):
            if remain == 0:
                output.append(path)
                return 
    
            for j in range(i,len(nums)):
                if remain < nums[i]:
                   return 
                dfs(j, path+[nums[j]], remain-nums[j])
        dfs(0, [],target)
        
        return output