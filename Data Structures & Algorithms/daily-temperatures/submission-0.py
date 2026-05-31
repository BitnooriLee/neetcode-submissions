class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stk = []
        #bf n*n 
        #stack 
        for i in range(len(temperatures)):
            while stk and (temperatures[i] > temperatures[stk[-1]]):
                idx = stk.pop()
                output[idx] = i - idx
            stk.append(i)

        return output

