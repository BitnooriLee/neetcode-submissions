class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        res = [] 
        candidates.sort()
        def bt(start, remain):
            if remain == 0:
                output.append(res[:])
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                res.append(candidates[i])
                bt(i+1,remain-candidates[i])
                res.pop()

        bt(0, target)

        return output

        