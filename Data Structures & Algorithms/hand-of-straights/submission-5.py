class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize !=0:
            return False
        cnt = Counter(hand)
        for i in sorted(cnt):
            need = cnt[i]
            for j in range(i, i+groupSize):
                cnt[j]-= need
                if cnt[j] < 0:
                    return False

        return True
            
        