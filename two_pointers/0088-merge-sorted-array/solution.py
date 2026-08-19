# Optimal Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        output = len(nums1) - 1
        while j > -1:
            if i > -1 and nums1[i] > nums2[j]:
                nums1[output] = nums1[i]
                i -= 1
            else:
                nums1[output] = nums2[j]
                j -= 1
            output -= 1
# Original Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        while -1 < i:
            nums1[i + n] = nums1[i]
            i -= 1
        output = 0
        i = n
        j = 0
        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j]:
                nums1[output] = nums1[i]
                i += 1
            else:
                nums1[output] = nums2[j]
                j += 1
            output += 1
        
        while j < n:
            nums1[output] = nums2[j]
            j += 1
            output += 1