# Cleaner Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            nums[output] = nums[i]
            output += 1
        return output
# Orginal Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[output] = nums[i]
            output += 1
        return output