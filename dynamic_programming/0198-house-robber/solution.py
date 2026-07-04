# Original Bottoms-up Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(1,len(nums)):
            j = i + 1
            dp[j] = max(dp[j-1], dp[j-2] + nums[i])
        
        return dp[-1]
# Optimal Soltuion
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = dp2 = 0

        for num in nums:
            dp3 = max(dp1, dp2 + num)
            dp2 = dp1
            dp1 = dp3
        
        return dp1
        