class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2: return [0]
        stk = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while (stk and stk[-1][0] < temperatures[i]):
                _, day = stk.pop()
                output[day] = i - day
            stk.append([temperatures[i],i])

        return output