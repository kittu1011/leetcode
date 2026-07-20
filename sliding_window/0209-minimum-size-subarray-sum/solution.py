class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        curr = 0
        curr_sum = 0
        result = len(nums) + 1
        for i, x in enumerate(nums):
            curr_sum += x
            curr += 1
            if curr_sum == target:
                result = min(result,curr)
            while curr_sum > target:
                j = i - (curr - 1)
                curr_sum -= nums[j]
                curr -= 1
        return result

Solution.minSubArrayLen(Solution(),7,[2,3,1,2,4,3])