class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        def dfs(path, i, remain):
            if remain == 0:
                output.append(path)
            
            if i >= len(candidates) or remain < candidates[i]:
                return 
            dfs(path+[candidates[i]],i+1, remain - candidates[i])
            while(i < len(candidates)-1 and candidates[i] == candidates[i+1]):
                i += 1 
            dfs(path,i+1, remain)

        dfs([],0,target)

        return output
            


        
        