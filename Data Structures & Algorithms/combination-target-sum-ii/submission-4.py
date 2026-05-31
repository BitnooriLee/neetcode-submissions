class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        candidates.sort()
        def bt(i, remain):
            if remain == 0:
                res.append(tmp[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j]==candidates[j-1]:
                    continue
                tmp.append(candidates[j])
                bt(j+1,remain - candidates[j])
                tmp.pop()
                
        bt(0, target)

        return res 