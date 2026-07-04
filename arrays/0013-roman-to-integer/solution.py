# Original Optimal Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            "I": 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = mp[s[-1]]
        for i in range(len(s) - 2, -1,-1):
            curr = mp[s[i]]
            nxt = mp[s[i+1]]
            if curr < nxt:
                result -= curr
            else:
                result += curr
        return result