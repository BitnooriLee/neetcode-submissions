class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        output = [0]*len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):
            if stk:
                while(stk and stk[-1][0] < t):
                    pt,pi = stk.pop()
                    output[pi] = i - pi
            stk.append((t,i))

        return output




        #온도가 높은 날중 현재랑 가장 가까이 있는날 스택 힌트!

        