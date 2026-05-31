class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        cnt1 = [0]*26
        cnt2 = [0]*26
        m,n = len(s1), len(s2)
        l=0
        need = len(set(s1))
        have = 0

        for ch in s1:
            cnt1[ord(ch)-ord('a')] += 1
            
        for r in range(n):
            idx2 = ord(s2[r]) - ord('a')

            cnt2[idx2]+=1 

            if cnt1[idx2] > 0:
                if cnt1[idx2] == cnt2[idx2]:
                    have+=1
                elif cnt1[idx2] == cnt2[idx2]-1:
                    have -=1 
            if r-l+1 > m:
                idx2_l = ord(s2[l]) - ord('a')
                if cnt1[idx2_l] > 0:
                    if cnt1[idx2_l] == cnt2[idx2_l]:
                        have-=1
                    elif cnt1[idx2_l]+1 == cnt2[idx2_l]:
                        have +=1 
                cnt2[idx2_l]-=1 
                l += 1
            if r-l+1 == m and have ==need:
                return True

        return False

        
        