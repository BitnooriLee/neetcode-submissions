class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        A,B = nums1, nums2

        if m > n:
            A,B = B,A 
            m,n = n,m 
    
        l,r = 0, m-1  
        half = (m+n)//2 # 내림하니까 항상 오른쪽이 더 많게 
        while(True): 
            i = l + (r-l)//2 #i mid 역할
            j = half - i - 2 
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < m else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m+n)%2 == 0:
                    return (max(Aleft, Bleft) + min((Aright,Bright)))/2 
                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1 