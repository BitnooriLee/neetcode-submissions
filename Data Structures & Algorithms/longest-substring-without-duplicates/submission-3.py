class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window 
        n = len(s)
        result,l = 0,0
        charSet = set()
        for r in range(n):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l+=1 
            charSet.add(s[r])
            result = max(result, r-l+1)
        return result