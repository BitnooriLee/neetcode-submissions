class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        
        for p, s in zip(position, speed):
            stk.append((p, (target - p) / s))
        
        stk.sort(reverse=True)  # position 큰 순서대로

        fleets = []
        for p, t in stk:
            if not fleets or t > fleets[-1]:
                fleets.append(t)
            # t <= fleets[-1] 이면 앞 차를 따라잡으므로 아무것도 안 함

        return len(fleets)
        