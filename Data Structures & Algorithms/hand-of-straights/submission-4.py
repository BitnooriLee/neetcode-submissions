class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l% groupSize != 0:
            return False
    
        cnt = Counter(hand)
        for i in sorted(cnt): #sort해서 작은것부터 groupSize만큼 센다 
            need = cnt[i]
            for v in range(i, i+groupSize):
                cnt[v]-= need
                if cnt[v] < 0:
                    return False
        return True

