class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dic = defaultdict(int)

        for s,e in intervals:
            for key in range(s,e+1):
                if dic[key] and dic[key] <= e-s+1:
                    continue
                dic[key] = e-s+1
                
        res= []

        for q in queries:
            if q in dic:
                res.append(dic[q])
            else:
                res.append(-1)

        return res 