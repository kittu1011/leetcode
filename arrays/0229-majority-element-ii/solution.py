class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = freq1 = freq2 = 0
        for x in nums:
            if x == cand1:
                freq1 += 1
            elif x == cand2:
                freq2 += 1
            elif freq1 == 0:
                cand1 = x
                freq1 = 1
            elif freq2 == 0:
                cand2 = x
                freq2 = 1
            else: # This else retires 3 elements in array (cand1,cand2,x)
                freq1 -= 1
                freq2 -= 1
        freq1 = 0
        freq2 = 0
        for x in nums: # need to validate cand1 and cand2 actually are apart of result
            if x == cand1:
                freq1 += 1
            elif x == cand2:
                freq2 += 1
        result = []
        if freq1 > len(nums) // 3:
            result.append(cand1)
        if freq2 > len(nums) // 3:
            result.append(cand2)
        return result