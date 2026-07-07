# Original Optimal Solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # partition the array into three segments
        l = 0 # [0,l) is all zeros
        r = len(nums) - 1 # (r,n-1] is all twos
        i = 0 # [l,i) is all ones and [i,r] are all elements that are unknown
        while i <= r: # [i,r] contains something
            ch = nums[i]
            if nums[i] == 0: # we can just swap with nums[l] as it's given to be 1 if i > l or 0 if i == l
                nums[i], nums[l] = nums[l], nums[i]
                l += 1 # increase [0,l) as we just added a zero to it
            elif nums[i] == 2: # we can just swap with nums[r]
                nums[i], nums[r] = nums[r], nums[i]
                i -= 1 # important nums[r] was unkonwn, so we must check it as nums[i] is unknown now as well
                r -= 1 # increase (r,n-1) as we just added a two to it
            i += 1