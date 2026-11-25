class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        for ch in s1:
            if ch not in s2:
                return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for ch in s1:
            cnt1[ord(ch) - ord('a')]+=1 
        k = len(s1)
        matches = 26 - len(set(s1)) # 0인건 일단 일치
        start = 0 
        for end in range(len(s2)):
            ce = ord(s2[end]) - ord('a')
            cnt2[ce]+=1 
            if cnt2[ce] == cnt1[ce]:
                matches +=1
            elif cnt2[ce] == cnt1[ce]+1: #같았다가 많아짐 
                matches -=1 
            
            if end >= k: #windows가 s1보다 커지면 
                cs = ord(s2[start]) - ord('a') #end-k 
                cnt2[cs]-=1 
                if cnt2[cs] == cnt1[cs]:
                    matches+=1
                elif cnt2[cs] +1 == cnt1[cs]:
                    matches-=1 
                start += 1 #end가 이미 커져서 필요없음 
            if matches == 26:
                return True

        return False

