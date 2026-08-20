# Optimal Soluton
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        l = 0
        r = m
        while l <= r:
            mid = (r - l) // 2 + l
            idx = half - mid
            right1 = nums1[mid] if 0 <= mid < m else float('inf')
            right2 = nums2[idx] if 0 <= idx < n else float('inf')
            left1 = nums1[mid-1] if 0 < mid else float('-inf')
            left2 = nums2[idx-1] if 0 < idx else float('-inf')
            if left1 > right2:
                r = mid - 1
            elif left2 > right1:
                l = mid + 1
            else:
                if (m + n) % 2 == 1:
                    return min(right1,right2)
                return (max(left1,left2) + min(right1,right2)) / 2
# Original Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        half = (m + n) // 2
        l = 0
        r = m
        while l < r:
            mid = (r - l) // 2 + l
            idx = half - mid
            if idx < 0:
                r = mid
                continue
            if idx > n:
                l = mid + 1
                continue
            print(mid,idx)
            if idx > 0 and idx <= n and nums2[idx-1] > nums1[mid]:
                l = mid + 1
            elif mid > 0 and idx < n and nums2[idx] < nums1[mid - 1]:
                r = mid
            else:
                break
        mid = (r - l) // 2 + l
        idx = half - mid
        print(mid,idx)
        a = nums1[mid] if 0 <= mid and mid < m else float('inf')
        b = nums2[idx] if 0 <= idx and idx < n else float('inf')
        print(a,b)
        if (m + n) % 2 == 1:
            return min(a,b)
        else:
            a1 = nums1[mid-1] if 0 < mid else float('-inf')
            b2 = nums2[idx-1] if 0 < idx else float('-inf')
            x = min(a,b)
            y = max(a1,b2)
            return (x + y) / 2