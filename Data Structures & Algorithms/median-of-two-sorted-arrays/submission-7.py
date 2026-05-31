class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2 
        n,m = len(nums1), len(nums2)

        if n > m :
            A,B = B,A #A shorter, reduce binary search 
            n,m = m,n

        half = (m+n+1)//2 # 홀수면 왼쪽에 한개가 더 가도록 셋팅     
        l,r = 0, n 
        while(l<=r):
            i = l + (r-l)//2 
            j = half - i 
            Aleft = A[i-1] if i > 0 else float("-inf") # i 가 왼쪽의 갯수 
            Aright = A[i] if i < n else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < m else float("inf")
            if Aleft <= Bright and Aright >= Bleft:
                return max(Aleft, Bleft) if (n+m)%2 == 1 else (max(Aleft, Bleft)+ min(Aright,Bright))/2
            elif Aleft > Bright:
                r = i - 1 
            else:
                l = i + 1



