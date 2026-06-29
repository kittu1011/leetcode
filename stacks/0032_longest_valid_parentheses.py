#Optimal Solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # INVARIANT: s[stk[-1] + 1: i] is a valid parentheses
        stk = [-1] # -1 is sentinel value we can think of it as before idx 0
        result = 0
        for i, ch in enumerate(s):
            if ch == '(': # s[i] cannot be apart of valid parentheses currently there stk[-1] == i in next iteration
                stk.append(i)
            else:
                stk.pop()
                if not stk: # unmatched ')' case means s[i] can NEVER be apart of a valid parentheses
                    stk.append(i) # therefore we append to stk and only care about valid parentheses starting at s[i+1]
                else: # matched ')' case therefore s[stk[-1]:i+1] is valid
                    result = max(result, i - stk[-1])
        return result
# Original stack Solution made with hint
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [] # contains only indicies for '(' along with the prev at that index 
        prev = 0 # prev is the longest valid parentheses ending at s[i - 1]
        result = 0
        for i,ch in enumerate(s):
            if ch == '(':
                stk.append((i,prev))
                prev = 0 # prev is 0 for next iteration as no valid parantheses ends with '('
            else:
                if not stk:
                    prev = 0 # next iteration prev is 0
                    continue
                # valid parantheses formed
                start, prev = stk[-1]
                add = (i - start) + 1 + prev # length of longest parantheses ending with s[i]
                stk.pop()
                result = max(add,result)
                prev = add # prev will be add for next iteration by definition
        return result
# Optimal bottoms up DP Solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        result = 0
        for i in range(1,len(s)):
            ch = s[i]
            if ch == '(': # base case
                continue
            if s[i-1] == '(': # handles ... + ()
                dp_2 = dp[i-2] if i > 1 else 0
                dp[i] = dp_2 + 2
            else: # handles ... + ))
                j = i - 1 - dp[i-1]
                if j >= 0 and s[j] == '(': # handles "((...))"
                    dp_3 = dp[j-1] if j > 0 else 0 # handles "..." + "((...))"
                    dp[i] = dp[i-1] + 2 + dp_3
            result = max(dp[i],result)
        
        return result