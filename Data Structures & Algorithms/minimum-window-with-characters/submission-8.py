class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        besti,bestj = 0,float("inf") 
        cnt_t = Counter(t)
        need = len(cnt_t)
        cnt_s = defaultdict(int)
        l = 0 
        have = 0 
        for r in range(len(s)):
            cnt_s[s[r]] += 1 
            if cnt_s[s[r]] == cnt_t[s[r]]:
                have += 1 
            while have == need:
                if (bestj - besti) > (r - l):
                    besti,bestj = l,r 
                cnt_s[s[l]] -= 1
                if cnt_s[s[l]] < cnt_t[s[l]]:
                    have -= 1 
                l+= 1 
   
        return s[besti:bestj+1] if bestj != float("inf") else ""


                
                
        
        