class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [(temperatures[0],0)]
        output = [0]*len(temperatures)

        for i in range(1, len(temperatures)):
            if stk:
                while stk and (stk[-1][0] < temperatures[i]):
                    (t, j) = stk.pop()
                    output[j] = i - j
                stk.append((temperatures[i],i))

        return output