# Original Optimal Solution
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for person in details:
            if int(person[-4:-2]) > 60:
                result += 1
        return result