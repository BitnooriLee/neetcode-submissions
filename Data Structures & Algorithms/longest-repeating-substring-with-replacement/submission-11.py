class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0]*26
        maxfreq = 0 
        l = 0
        output = 0 
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            cnt[idx]+=1 
            maxfreq = max(maxfreq,cnt[idx])

            while(r-l+1 -maxfreq > k):
                cnt[ord(s[l]) - ord('A')]-=1 
                l += 1 
            output = max(output, r-l+1)
        return output 
        