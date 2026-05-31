class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        check = [float("inf")]*1000 # querise only 1>= int 

        for l,r in intervals:
            for cur in range(l,r+1):
                dis = r - l +1 
                check[cur] = min(dis,check[cur])
        
        for q in queries:
            if check[q] != float("inf"):
                output.append(check[q])
            else:
                output. append(-1)

        return output


        