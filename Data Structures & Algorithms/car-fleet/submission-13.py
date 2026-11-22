class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        for p,s in sorted(zip(position,speed), reverse=True):
            if not stk or (target - p)/s > stk[-1][1]:
                stk.append((p,(target - p)/s))

        return len(stk)

        