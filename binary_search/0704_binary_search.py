# Classic binary search [l,h)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1
# Classic binary search [l,h]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1