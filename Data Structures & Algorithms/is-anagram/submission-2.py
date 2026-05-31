class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        dic_s = {}
        dic_t = {}
        for ss in s: 
            dic_s[ss] = dic_s.get(ss, 0)+1 
        for tt in t:
            dic_t[tt] = dic_t.get(tt, 0)+1 
        for k in dic_s.keys():
            if k not in dic_t.keys():
                return False
            if dic_t[k] != dic_s[k]:
                return False
        return True


            
        
        