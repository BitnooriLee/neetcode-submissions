class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        def dfs(path,i):
            if i >= len(nums):
                output.append(path)
                return
            dfs(path+[nums[i]], i+1)
            while i < len(nums)-1 and (nums[i] == nums[i+1]):
                i += 1 
                
            dfs(path, i+1)

        dfs([],0)
        
        return output

        