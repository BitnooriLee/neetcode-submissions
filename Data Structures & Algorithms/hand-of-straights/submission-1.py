class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand) 
        if l % groupSize != 0:
            return False

        cnt = Counter(hand)

        for x in sorted(cnt): # 여기가 포인트 
            if cnt[x] > 0:
                need = cnt[x]
                for v in range(x, x+groupSize):
                    cnt[v] -= need
                    if cnt[v] < 0:
                        return False
                    

        return True


        