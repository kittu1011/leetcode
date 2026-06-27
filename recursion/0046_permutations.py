# Original Optimal Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def helper(i):
            if i == len(nums):
                result.append(path.copy())

            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                path.append(nums[i])
                helper(i + 1)
                path.pop()
                nums[i], nums[j] = nums[j], nums[i]

        helper(0)
        return result