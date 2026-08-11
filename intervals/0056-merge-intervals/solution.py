class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda interval: interval[0])
        result = []
        for x in intervals_sorted:
            if result and x[0] <= result[-1][1]:
                result[-1][1] = max(x[1],result[-1][1])
            else:
                result.append(x)
        return result