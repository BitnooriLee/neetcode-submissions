class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []


        def bt(i,t,tmp):
            if t == 0:
                output.append(tmp[:])
                return
            if i >= len(candidates) or t < 0:
                return
            #i 포함
            tmp.append(candidates[i])
            bt(i+1,t-candidates[i],tmp)
            tmp.pop()
            #i 안포함 
            while(i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            bt(i+1,t,tmp)

        bt(0,target,[])
        return output