class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1


        # 누적 += gas[i]-cost[i] 이게 계속 + 여야 함 음수면 그다음으로, 시작할때 누적은 0 
        cur = 0
        position = 0 
        for i in range(len(gas)):
            cur += gas[i] - cost[i]

            if cur < 0:
                cur = 0 
                position = i+1 
        
        return position
        