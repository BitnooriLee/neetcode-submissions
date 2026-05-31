class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        check = [-1]*10001 

        
        intervals.sort(key= lambda x: x[1] - x[0])

        for s,e in intervals:
            for i in range(s,e+1):
                if check[i] != -1:
                    continue
                else:
                    check[i] = e-s+1

        res = []


        for q in queries:
            res.append(check[q])

        return res 
                