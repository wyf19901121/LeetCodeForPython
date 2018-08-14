class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)

        if length % 2 == 0:
            return (float(self.findKthSortedArrays(nums1, nums2, length/2))
                    + float(self.findKthSortedArrays(nums1, nums2, length / 2 - 1))) / 2
        else:
            return self.findKthSortedArrays(nums1, nums2, length/2)

    def findKthSortedArrays(self, nums1, nums2, index):
        if len(nums1) > len(nums2):
            return self.findKthSortedArrays(nums2, nums1, index)
        if len(nums1) == 0:
            return nums2[index]
        if index == 0:
            return min(nums1[0], nums2[0])

        index1 = min(index / 2, len(nums1) - 1)
        index2 = index - index1 - 1

        if nums1[index1] == nums2[index2]:
            return nums1[index1]
        elif nums1[index1] > nums2[index2]:
            return self.findKthSortedArrays(nums1, nums2[index2 + 1:len(nums2)], index - index2 - 1)
        else:
            return self.findKthSortedArrays(nums1[index1 + 1:len(nums1)], nums2, index - index1 - 1)



