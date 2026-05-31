class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]

        pair.sort(reverse=True) # check right to left 

        stk = []

        for p,s in pair:
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]: #left faster than right, remove left (fleet)! 
                stk.pop()
        return len(stk)
            
        