# Original Inefficient Solution
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort_pos = 0
        n = len(nums)
        for i in range(n-1,-1,-1):
            flag = False
            for j in range(n-1,i,-1):
                if (nums[j] > nums[i]):
                    sort_pos = i + 1
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp 
                    flag = True
                    break
            if flag:
                break
        nums[sort_pos:] = sorted(nums[sort_pos:])
# Elegant Optimal solution
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - 2

        while pivot > -1 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        if pivot > -1:
            for i in range(n-1,pivot,-1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        
        nums[pivot+1:] = reversed(nums[pivot+1:])  