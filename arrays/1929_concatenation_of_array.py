# Original explicit solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i in range (2 * n):
            result[i] = nums[i % n]
        return result

# Production solution 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Cleanest solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[i % n] for i in range(2 * n)]