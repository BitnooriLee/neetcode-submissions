class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        for num in sorted(cnt):
            need = cnt[num]
            for j in range(num, num+groupSize):
                cnt[j] -= need
                if cnt[j] < 0:
                    return False
        return True
        