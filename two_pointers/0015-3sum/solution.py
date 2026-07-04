# Optimal Solution
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0: # if the smallest int in the triplet is positive then it's impossible for it to sum to zero
                break
            target = 0 - nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    result.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1                    
                    while l < r and nums[l-1] == nums[l]: l += 1
                    while l < r and nums[r+1] == nums[r]: r -= 1
                elif curr > target:
                    r -= 1
                else:
                    l += 1
        return result