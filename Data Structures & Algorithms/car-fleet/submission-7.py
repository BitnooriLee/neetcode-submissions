class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse= True) # 앞에 있는거 부터 
        stk = []
        for p,s in pair:
            stk.append((target - p)/s)
            if len(stk) > 1 and stk[-2] >= stk[-1]:
                stk.pop()
        return len(stk)


        