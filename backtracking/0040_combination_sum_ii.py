# Original Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        results = []
        path = []

        def helper(i,t):
            if t == 0: # this base case MUST come before the next one as it allows for solutions that use candidates[0] which call helper(-1,t-candidates[0])
                results.append(path.copy())
                return
            if i < 0 or t < 0:
                return
            
            path.append(candidates[i])
            helper(i-1,t-candidates[i])
            path.pop()

            j = i - 1
            while j > -1 and candidates[i] == candidates[j]: 
                j -= 1
            helper(j,t)

        helper(len(candidates) - 1, target)
        return results
# Elegant Optimal Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        path = []
        def helper(i,t):
            if t == 0:
                results.append(path.copy())
                return
            
            for j in range(i, len(candidates)):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > t:
                    break
                path.append(candidates[j])
                helper(j + 1, t - candidates[j]) # goes in opposite direction as first solution
                path.pop()

        helper(0, target)
        return results