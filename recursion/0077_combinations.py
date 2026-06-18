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
