# Original Optimal Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        result = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            result += 1
        
        return result
# Cleanest solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) # works because split will ignore whitespaces by default