# Original Optimal Solution
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (r - l) // 2 + l
            est = 1
            curr = 0
            for w in weights:
                if curr + w > mid:
                    est += 1
                    curr = 0
                curr += w
            
            if est > days:
                l = mid + 1
            else:
                r = mid - 1
        return l