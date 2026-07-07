# Original one pass solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        result = 0
        for x in nums:
            if x in mp:
                continue
            l = mp.get(x-1,0) # check longest sequence to the left
            r = mp.get(x+1,0) # check longest sequence to the right
            s = l + r + 1
            mp[x-l] = s # update start of sequence
            mp[x+r] = s # update end of sequence
            mp[x] = s # mark x as seen
            result = max(result,s)
        return result
# Cleaner two-pass solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0
        for x in s:
            if x - 1 in s:
                continue
            curr = 1
            while x + curr in s:
                curr += 1
            result = max(result,curr)
        return result