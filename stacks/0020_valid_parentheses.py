# Original optimal solution
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        bracket_map = {")" : "(", "}" :"{", "]" : "["}
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            else:
                if not stk or stk[-1] != bracket_map[ch]:
                    return False
                stk.pop()
        return stk == []