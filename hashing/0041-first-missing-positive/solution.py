# Negative Marking solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1:
                nums[i] = n + 1 #should not use zero as sentinel value as it can't have a sign
        # sign of element indicates weather or not element i + 1 exists
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            index = val - 1
            nums[index] = abs(nums[index]) * -1
        
        result = n + 1
        for i, x in enumerate(nums):
            if x > 0: # if elements does not exist in hash
                return i + 1
        return result
# cycle sort solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            if val < 1 or val > n: # elements is don't care or out of bounds
                i += 1
                continue
            j = val - 1 # "hashed" index 
            if val != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else: # element exists in hash
                i += 1
        
        result = n + 1
        for i, x in enumerate(nums):
            if x != i + 1: # if elements does not exist in hash
                return i + 1
        return result
# hash set solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 1
        while result in seen:
            result += 1
        return result
