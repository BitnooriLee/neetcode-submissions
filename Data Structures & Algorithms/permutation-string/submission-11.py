class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)

        cnt1 = [0]*26
        cnt2 = [0]*26 

        for ch in s1:
           cnt1[ord(ch)-ord('a')]+=1 
        
        l = 0 
        need = len(set(s1))
        have = 0 
        for r in range(n):
            cnt2[ord(s2[r])-ord('a')]+=1 
            if cnt2[ord(s2[r])-ord('a')] == cnt1[ord(s2[r])-ord('a')]:
                have += 1
            elif cnt2[ord(s2[r])-ord('a')] == cnt1[ord(s2[r])-ord('a')] + 1:
                have -= 1
            if r - l + 1 > m: #l을 올릴거.. 애초에 m 보다 작으면 연산x 
                if cnt2[ord(s2[l])-ord('a')] == cnt1[ord(s2[l])-ord('a')]:
                    have -= 1 
                elif cnt2[ord(s2[l])-ord('a')] == cnt1[ord(s2[l])-ord('a')]+1:
                    have += 1 
                cnt2[ord(s2[l])-ord('a')] -= 1
                l+= 1
                
            if need == have and (r-l+1) == m:
                return True 
        return False




        


        