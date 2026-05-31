class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_cnt = defaultdict(int)
        l = 0
        maxf = 0 

        for r in range(len(s)):
            ch_cnt[s[r]] = ch_cnt.get(s[r],0)+1 
            maxf = max(maxf,ch_cnt[s[r]])
            if r - l +1 -maxf > k:
                ch_cnt[s[l]] -= 1 
                l += 1 
            
        return r - l +1 
        