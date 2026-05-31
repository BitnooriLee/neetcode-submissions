class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        if sum(gas) < sum(cost):
            return -1
        i = 0 
        while(i<l):
            pre = 0 
            for j in range(i,i+l):
                k = j%l
                print(k)
                if pre + gas[k] - cost[k] < 0:
                    break
                pre = pre + gas[k] - cost[k]
                if j == i+l-1:
                    return i
            i += 1 
        return -1