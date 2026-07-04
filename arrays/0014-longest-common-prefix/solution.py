# Original Optimal solution O(n * m), where m is len of shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i, ch in enumerate(strs[0]):
            for word in strs:
                if i == len(word) or word[i] != ch:
                    return result
            result += ch
                
        return result
# Sorting solution O(nlogn * m)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs = sorted(strs)
        word = strs[-1]
        for i, ch in enumerate(strs[0]):
            if i == len(word) or word[i] != ch:
                return result
            result += ch
                
        return result