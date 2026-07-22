class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # when you get rid of prefix sum at index i you consider nums[i+1:]
        freq = {0: 1} # having this value allows for us to consider subarray starting at index 0. Think of it as prefix of before the array
        curr_sum = 0 # culminating sum
        result = 0

        for x in nums:
            curr_sum += x
            result += freq.get(curr_sum - k, 0)
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        return result