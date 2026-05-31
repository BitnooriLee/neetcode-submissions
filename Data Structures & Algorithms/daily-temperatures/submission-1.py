class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] 
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                sT, sI = stk.pop()
                res[sI] = i - sI
            stk.append((t,i))

        return res
        