# Original sup-optimal solution with O(n) space complexity
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i = 0
        left_max = height[0]
        right_max = height[-1]
        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(len(height)):
            l = height[i]
            r = height[-1 - i]

            left_max = max(left_max,l)
            right_max = max(right_max,r)

            left[i] = left_max
            right[-1 - i] = right_max
        result = 0
        for i in range(1,len(height)-1):
            if (min(left[i-1],right[i+1]) - height[i]) > 0:
                result += min(left[i-1],right[i+1]) - height[i] # The most amount of water height[i] holds is min of it's left and right max
        return result
# Optimal solution made with help
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i = 0
        left_max = height[0]
        right_max = height[-1]
        l = 0
        r = len(height) - 1

        while l < r:
            if left_max < right_max:
                if height[l+1] >= left_max:
                    left_max = height[l+1]
                else:
                    result += left_max - height[l+1]
                l += 1
            else:
                if height[r-1] >= right_max:
                    right_max = height[r-1]
                else:
                    result += right_max - height[r-1]
                r -= 1
        return result
