# Unconventional Memoization solution as it builds strings from right to left (i.e compares "ab" to "*b*")
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        dp = [[-1] * (m + 2) for _ in range(n + 1)]
        dp[-1][-2] = 1 # Base case with two empty strings
        def helper(i,j):
            if dp[i][j] != -1: # if it already exists in dp
                return dp[i][j]
            
            if j >= m: # i < n but p is empty so automatic fail
                dp[i][j] = 0
                return dp[i][j]

            if j + 1 < m and p[j+1] == '*':
                dp[i][j] = helper(i,j+2) # zero characters of p[j]
                # one or more characters of p[j]
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = max(dp[i][j],helper(i+1,j))
                
                return dp[i][j]
            
            if  i < n and (s[i] == p[j] or p[j] == '.'): # no star case but match
                dp[i][j] = helper(i+1,j+1)
                return dp[i][j]
            
            dp[i][j] = 0 # no star but no match so letters don't match
            return 0
        
        return bool(helper(0,0))
#Unconventional Bottoms up solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        dp[-1][-1] = True

        for i in range(len(s),-1,-1):
            for j in range(len(p) - 1,-1,-1):
                star = j < len(p) - 1 and p[j+1] == '*'
                mtch = i < len(s) and (s[i] == p[j] or p[j] == '.')
    
                if mtch and not star:
                    dp[i][j] = dp[i+1][j+1]
                elif not mtch and star:
                    dp[i][j] = dp[i][j+2]
                elif mtch and star:
                    dp[i][j] = dp[i][j+2] or dp[i+1][j]

        return dp[0][0]

Solution.isMatch(Solution(), "aa", "a*")