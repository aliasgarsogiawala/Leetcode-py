class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3=nums1+nums2
        num3.sort()
        n=len(num3)
        if n % 2 == 1:  
            median = num3[n // 2]
        else:  
            mid1 = num3[n // 2 - 1]
            mid2 = num3[n // 2]
            median = (mid1 + mid2) / 2.0
        return median