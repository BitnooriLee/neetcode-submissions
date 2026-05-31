class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def dfs(path, cur):
    
            if sum(path) > target:
                return
            if sum(path) == target:
                output.append(path)

            prev = 0 
            for i in range(cur,len(candidates)):
                if prev != candidates[i]:
                    dfs(path+[candidates[i]], i+1)
                prev = candidates[i]

        dfs([],0)

        return output

        



