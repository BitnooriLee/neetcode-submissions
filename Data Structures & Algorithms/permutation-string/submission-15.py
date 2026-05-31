class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        l = 0
        cnt1 = [0]*26
        cnt2 = [0]*26
        need = len(set(s1))
        have = 0 

        for ch in s1:
            cnt1[ord(ch)-ord('a')] += 1
            
        for r in range(len(s2)):
            ir = ord(s2[r]) - ord('a')
            cnt2[ir]+=1
            if cnt1[ir] > 0: 
                if cnt2[ir] == cnt1[ir]:
                    have += 1 
                if cnt2[ir] == cnt1[ir] + 1:
                    have -= 1 
            if r-l+1 > m:
                il = ord(s2[l]) - ord('a')
                if cnt1[il] > 0: 
                    if cnt2[il] == cnt1[il]:
                        have -= 1 
                    if cnt2[il] == cnt1[il] + 1:
                        have += 1 
                cnt2[il]-=1
                l+=1
            if r-l+1 == m and have == need:
                return True

        return False



#1. dic대신 list로도 가능 lowercase니까   



        