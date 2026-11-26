class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        
        need = Counter(t)
        have = defaultdict(int)
        l = 0 
        matches = 0
        #minl, minr = 0, len(s)-1
        best_len, best_l = float("inf"), 0 

        for r in range(len(s)):
            have[s[r]] += 1 
            if s[r] in need and have[s[r]]==need[s[r]]:
                matches += 1      
            while matches == len(need): #유효한 동안 줄이기, 줄이기 전 답 갱신 
                if r - l + 1 < best_len:
                    best_len, best_l = r-l+1, l
                have[s[l]]-=1
                if s[l] in need and have[s[l]]+1 == need[s[l]]:
                    matches -= 1 
                l+=1
        return "" if best_len == float("inf") else s[best_l:best_l+best_len] 
            
            
        
        