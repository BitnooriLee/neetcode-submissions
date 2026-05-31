class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtracking(start, remain):
            if remain == 0:
                res.append(path[:])
                return 
            if remain < 0:
                return 
            
            prev = None
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                path.append(candidates[i])
                prev = candidates[i]
                backtracking(i+1, remain - candidates[i])
                path.pop()

        backtracking(0, target)

        return res
        