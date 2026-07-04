# Original Optimal solution
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        n = len(arr)
        res = [0] * n
        for i in range(n-1, -1, -1):
            res[i] = curr_max
            curr_max = max(curr_max,arr[i])
        return res
        