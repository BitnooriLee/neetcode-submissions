from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = defaultdict(int)
        
        for ch in s:
            dic[ch]+=1
        for ch in t:
            dic[ch]-=1
            if dic[ch] <0:
                return False
        return True



            
        
        