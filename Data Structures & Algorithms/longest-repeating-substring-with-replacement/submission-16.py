class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        max_freq = 1
        res = 0
        cnt = defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]]+= 1 
            max_freq = max(max_freq,cnt[s[r]])
            while r-l+1 - max_freq > k:
                cnt[s[l]]-=1
                l += 1 
            res = max(res, r-l+1)
        return res
            
        