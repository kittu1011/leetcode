# Original Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        result = nums[0]
        for x in nums[1:]:
            if not count:
                result = x
            if result == x:
                count += 1
            else:
                count -= 1
        return result