class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_s1 = [0]*26
        dic_s2 = [0]*26

        for ch in s1:
            dic_s1[ord(ch) - ord('a')] += 1 

        for i in range(len(s2)):
            dic_s2[ord(s2[i]) - ord('a')] += 1 
            if i >= len(s1):
                dic_s2[ord(s2[i-len(s1)]) - ord('a')] -= 1 
            if dic_s2 == dic_s1:
                return True

        return False
                

    

        