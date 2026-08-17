# Original Optimal Solution
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (r - l) // 2 + l
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                r = mid - 1
            else:
                l = mid + 1
        return -1