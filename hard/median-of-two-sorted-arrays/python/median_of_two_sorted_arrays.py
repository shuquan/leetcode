class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i = i + 1
            else:
                merged.append(nums2[j])
                j = j + 1
        if i == len(nums1):
            merged.extend(nums2[j:])
        else:
            merged.extend(nums1[i:])
        quotient, remainder = divmod(len(merged), 2)
        if remainder is 1:
            return merged[quotient]
        elif remainder is 0:
            return (merged[quotient - 1] + merged[quotient])/2.0
