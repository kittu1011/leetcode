# Optimal Solution
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = -(sum(piles) // -h)
        r = max(piles)
        while l <= r:
            mid = (r - l) // 2 + l
            est = 0
            for x in piles:
                est += -(x // -mid)
            if est > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
# Original Solution
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(piles: List[int], k: int):
            if k == 0:
                return float('inf')
            hours = 0
            for x in piles:
                hours += -(x // -k)
            return hours
        
        l = 1
        r = max(piles)
        while l <= r:
            mid = (r - l) // 2 + l
            est = helper(piles,mid)
            print(mid, l, r)
            if est <= h and helper(piles,mid-1) > h:
                return mid
            if est > h:
                l = mid + 1
            else:
                r = mid - 1
        print(helper(piles,14))
        return -1