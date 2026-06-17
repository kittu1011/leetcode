# Original Optimal Solution
class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch == '*' and result:
                result = result[:-1]
            elif ch == '#':
                result  *= 2
            elif ch == '%':
                result = result[::-1]
            elif ch != '*':
                result += ch
        
        return result
