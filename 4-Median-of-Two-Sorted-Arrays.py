class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m= []
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                m.append(nums1[i])
                i+=1
            else:
                m.append(nums2[j])
                j+=1
        m.extend(nums1[i:])
        m.extend(nums2[j:])
        length= len(m)
        if length%2==0:
            return (m[length//2 -1]+m[length//2])/2
        else:
            return m[length//2]