class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        path = []
        def bt(i,remain):
            if remain == 0:
                output.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j-1] == candidates[j]:
                    continue
                path.append(candidates[j])
                bt(j+1,remain-candidates[j])
                path.pop()

        bt(0, target)
        
        return output

        