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
                #여기서 i인경우 한번만 더해줬음..! 그 다음 j 부터 체크
                tmp.append(candidates[j])
                bt(j+1,remain - candidates[j])
                tmp.pop()
                
        bt(0, target)

        return res 