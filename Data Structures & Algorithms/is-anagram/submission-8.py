class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        
        for k in cnt_s.keys():
            if cnt_t[k] != cnt_s[k]:
                return False
        return True
        