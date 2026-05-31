class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        check = [float("inf")]*(max(e for s,e in intervals)+1)
        res = []
        for inter in intervals:
            s,e = inter
            for i in range(s,e+1):
                if check[i] > e-s+1:
                    check[i] = e-s+1
        for q in queries:
            if q >= len(check):
                res.append(-1)
            elif check[q] != float("inf"):
                res.append(check[q])
            else:
                res.append(-1)

        return res


        