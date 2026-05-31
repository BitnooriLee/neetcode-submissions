class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m,n = n,m 

        A = nums1
        B = nums2 
        half = (m+n)//2
        l,r = 0, m-1
        while(True):
            i = l + (r-l)//2 
            j = half - i -2
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < m else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright =  B[j+1] if j+1 < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m+n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2 
                else:
                    return min(Aright, Bright)
            
            if Aleft > Bright:
                r = i - 1
            if Aright < Bleft:
                l = i + 1 


        