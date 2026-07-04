# Original but messy solution
class Solution1:
    def minInsertions(self, s: str) -> int:
        left = 0 # count of open '('
        i = 0
        result = 0
        while i < len(s):
            ch = s[i]
            if ch == '(':
                left += 1
                i += 1
                continue
            num = -0.5 # -0.5 -> ')'  
            if i + 1 < len(s) and s[i+1] == ')': # gets consecutive ')' if possible
                num = -1 # -1 -> '))'
                i += 1
            # high-level idea: find imbalances such as '))','()',')' that cannot be balanced by subsequent characters and balance them immediately 
            temp = int(left > 0) # if left > 0 then temp -> '(' otherwise ''
            left -= temp # eats open parantheses
            num += temp # concatenates open and close parantheses
            if num == 0.5 or num == -1: # num represents '()' or '))' which are balanced by only one insertion
                result += 1
            elif num == -0.5: # num represents ')' which are balanced by two insertions
                result += 2
            i += 1

        return result + left * 2 # any remaining '(' need two insertions
# Most elegant and optimal solution
class Solution:
    def minInsertions(self, s: str) -> int:
        close_needed = 0
        insertions = 0
        for ch in s:
            if ch == '(':
                if close_needed % 2 == 1: # takes care of '()(' case
                    insertions += 1 # insert ')'
                    close_needed -= 1 # need one less ')' after insertion
                close_needed += 2
            else:
                if close_needed == 0: # handles ')'
                    insertions += 1 # insert '('
                    close_needed += 2 # need two more ')' to inserted '(' 
                close_needed -= 1 # consume one ')'

        return insertions + close_needed
