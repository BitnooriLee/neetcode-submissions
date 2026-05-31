class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if m < n :
            return ""
        set_t = set(t)
        set_s = set(s)

        for ch in set_t:
            if ch not in set_s:
                return ""

        cnt_t = defaultdict(int)
        for ch in t:
            cnt_t[ch] += 1
        l = 0 
        besti, bestj = 0, float("inf")
        need = len(set_t)
        have = 0 
        cnt_s = defaultdict(int)

        for r in range(m):
            
            cnt_s[s[r]] +=1 
            if cnt_s[s[r]] == cnt_t[s[r]]:
                have += 1 
            while need == have:
                if r-l+1 < bestj-besti+1:
                    besti,bestj = l,r
                cnt_s[s[l]]-=1
                if cnt_s[s[l]] < cnt_t[s[l]]:
                    have -= 1
                l+=1 
        return s[besti:bestj+1] if bestj != float("inf") else ""
                
            



                