class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dic = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]]+1
            dic[s[r]] = r 
            output = max(output, r-l+1)
            
        return output

#현재 윈도우 l,r 