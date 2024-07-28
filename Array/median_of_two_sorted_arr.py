class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge=nums1+nums2
        n=len(merge)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if merge[j]<merge[min_index]:
                    min_index=j
            merge[i],merge[min_index]=merge[min_index],merge[i]


        if n%2!=0:
            return merge[n//2]
        else:
            even1=merge[n//2]
            even2=merge[(n//2)-1]
            return float(even1+even2)/2
