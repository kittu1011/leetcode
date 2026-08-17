# Original Optimal Solution
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (r - l) // 2 + l
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1