class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(path, remain):
            if remain == 0:
                output.append(path)
                return 
            if remain < 0 :
                return 
            for num in nums:
                if not path:
                    dfs(path+[num], remain-num)
                elif path[-1] <= num:
                    dfs(path+[num], remain-num)
        dfs([],target)
        
        return output