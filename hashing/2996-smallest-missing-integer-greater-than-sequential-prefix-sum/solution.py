# Original Optimal Solution
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        hsh = set(nums)
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
            curr += nums[i]

        while curr in hsh:
            curr += 1
        return curr