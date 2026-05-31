class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def dfs(path, cur):
            if sum(path) == target:
                output.append(path)
            if sum(path) > target:
                return 

            for i in range(cur,len(nums)):
                dfs(path+[nums[i]], i)

        dfs([],0)


        return output 
        