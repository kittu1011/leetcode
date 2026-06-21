# Original Optimal Solution
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []

        def helper(x,y):
            if y == 0:
                result.append(path.copy())
                return
          
            for z in range (x+1,n-y+2):
                path.append(z)
                helper(z,y-1)
                path.pop()
    
        helper(0,k)
        return result
# Optimized Elegant soluton
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        def helper(i,t):
            if t == 0:
                results.append(path.copy())
                return
            
            for j in range(i,-1,-1):
                if t - candidates[j] < 0:
                    continue
                path.append(candidates[j])
                helper(j,t - candidates[j])
                path.pop()
        
        helper(len(candidates) - 1, target)
        return results
