class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrival time
        stk = []
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse= True)

        for p,s in pair:
            stk.append((target-p)/s)
            if len(stk) > 1 and stk[-1] <= stk[-2]:
                stk.pop()
            
        return len(stk)
        


            
            

        