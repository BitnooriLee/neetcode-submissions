class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []

        
        for p,s in zip(position,speed):
            stk.append((p, (target-p)/s))
        
        stk.sort(reverse = True)

        fleets = []

        for p,t in stk:
            if not fleets or t > fleets[-1]:
                fleets.append(t)
                
            
        return len(fleets)
        
        
        