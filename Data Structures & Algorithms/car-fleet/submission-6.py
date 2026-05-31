class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)

        for (p,s) in pairs:
            stk.append((target-p)/s)
            if len(stk)>=2 and stk[-2] >= stk[-1]:
                stk.pop() #따라잡고 본인은 없어짐. merge 됨 .. 자동으로 어차피 그담들어올 애가 또 따라잡으면 또 팝 
        return len(stk)
        

    

    #O(n) -> O(nlogn) sort!! 
    #O(n)