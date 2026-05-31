class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        cnt_s = defaultdict(int)
        m, n = len(s), len(t)
        if m < n: return ""

        need = len(cnt_t)
        have, l = 0,0 
        best_i, best_j = 0, float("inf")
        for r in range(m):
            cnt_s[s[r]]+= 1 
            if s[r] in cnt_s and cnt_s[s[r]] == cnt_t[s[r]]:
                have += 1
            while need == have:
                if (r - l + 1) < (best_j - best_i +1):
                    best_i, best_j = l, r
                cnt_s[s[l]]-= 1   
                if cnt_s[s[l]] < cnt_t[s[l]]:
                    have -= 1 
                l+=1 

        return s[best_i:best_j+1] if best_j != float("inf") else ""

            
        