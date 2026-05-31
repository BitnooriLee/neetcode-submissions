class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        cnt_t = Counter(t)
        need =len(cnt_t)
        have = 0
        l = 0
        cnt_s = defaultdict(int)
        besti,bestj = 0, float("inf")
        for r in range(len(s)):
            cnt_s[s[r]]+=1 
            if cnt_t[s[r]] == cnt_s[s[r]]:
                have +=1 
            while have == need:
                if r-l+1 < bestj-besti+1:
                    besti, bestj = l,r
                cnt_s[s[l]]-=1 
                if cnt_t[s[l]] > cnt_s[s[l]]:
                    have -=1 
                l+=1 
        
        return s[besti:bestj+1] if bestj != float("inf") else ""