#Original Optimal Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                result = max(result,curr)
            else:
                curr = 0
        
        return result