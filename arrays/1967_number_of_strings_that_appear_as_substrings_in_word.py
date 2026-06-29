# Original Optimal Solution
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for w in patterns:
            if w in word:
                result += 1
        return result