class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        bestl,bestr = 0,0

        def expend(l,r):
            nonlocal bestl, bestr
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r - l > bestr - bestl:
                    bestr,bestl = r, l
                l -= 1
                r += 1


        for i in range(len(s)):
            expend(i,i)
            expend(i,i+1)

        return s[bestl:bestr+1]
        