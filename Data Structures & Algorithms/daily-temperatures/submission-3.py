class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0]*len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            while stk and (stk[-1][0] < temperatures[i]):
                (t, j) = stk.pop()
                output[j] = i - j
            stk.append((temperatures[i],i))

        return output