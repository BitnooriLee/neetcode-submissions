class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt_s1 = [0] * 26
        cnt_s2 = [0] * 26
        for ch in s1:
            cnt_s1[ord(ch) - ord("a")] += 1 

        l = 0 
        need = len(set(s1))
        have = 0 
        for r in range(len(s2)):
            if cnt_s1[ord(s2[r])- ord("a")] > 0:
                cnt_s2[ord(s2[r])- ord("a")]+=1 
                if cnt_s2[ord(s2[r])- ord("a")] == cnt_s1[ord(s2[r])- ord("a")]:
                    have += 1
                elif cnt_s2[ord(s2[r])- ord("a")] == cnt_s1[ord(s2[r])- ord("a")]+1:
                    have -= 1
            if (r-l+1 > len(s1)):
                if cnt_s1[ord(s2[l])- ord("a")] > 0:
                    if cnt_s2[ord(s2[l])- ord("a")] == cnt_s1[ord(s2[l])- ord("a")]:
                        have -= 1
                    elif cnt_s2[ord(s2[l])- ord("a")] == cnt_s1[ord(s2[l])- ord("a")]+1:
                        have += 1
                cnt_s2[ord(s2[l])- ord("a")]-=1 
                l +=1
                    

            if r-l+1 == len(s1) and need == have:
                return True

        return False 
        