# Original Merge Sort Solution
class Solution2:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(nums, l: int, r: int):
            m = (r - l) // 2 + l
            # shallow copies will not modify original nums
            left, right = nums[l:m+1], nums[m+1:r+1] # easier to split the copy into two, then one
            i, j, k = 0, 0, l

            while i <len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            
        def merge_sort(nums, l: int, r: int):
            if l >= r: # don't need r - l == 1 as a base case as merge can handle that
                return
            m = (r - l) // 2 + l
            merge_sort(nums, l, m)
            merge_sort(nums, m + 1, r)
            merge(nums, l, r)
        
        merge_sort(nums, 0, len(nums) - 1)
        return nums
# Quick sort solution
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, l, r):
            m = (r - l) // 2 + l
            if nums[l] > nums[m]: # 3way partition
                nums[l], nums[m] = nums[m], nums[l]
            if nums[m] > nums[r]:
                nums[m], nums[r] = nums[r], nums[m]
            if nums[l] > nums[m]:
                nums[l], nums[m] = nums[m], nums[l]

            nums[r], nums[m] = nums[m], nums[r]
            pivot = r
            pivot_val = nums[pivot]
            r -= 1
            while l < r:
                if nums[l] >= pivot_val and nums[r] <= pivot_val:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                while l < r and nums[l] < pivot_val:
                    l += 1
                while l < r and nums[r] > pivot_val:
                    r -= 1
            if nums[l] > pivot_val:
                nums[pivot], nums[l] = nums[l], nums[pivot]
                return l
            nums[pivot], nums[r+1] = nums[r+1], nums[pivot] # if nums[l] is not greater it's guranteed that nums[r+1] is >= pivot_value
            return r + 1
            
        def quick_sort(nums,l,r):
            if l >= r:
                return
            while l < r: # this small optimization allows me recurse into bigger half from the parent's stack frame itself
                m = partition(nums,l,r)
                if m - l < r - m:
                    quick_sort(nums,l,m-1)
                    l = m + 1
                else:
                    quick_sort(nums,m+1,r)
                    r = m - 1

        quick_sort(nums,0,len(nums)-1)
        return nums