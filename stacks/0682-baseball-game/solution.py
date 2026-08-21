class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for x in operations:
            if x == 'D':
                stk.append(stk[-1] * 2)
            elif x == 'C':
                stk.pop()
            elif x == '+':
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(x))
        return sum(stk)