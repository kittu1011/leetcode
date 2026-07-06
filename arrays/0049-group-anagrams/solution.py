class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        result = []
        for s in strs:
            t = "".join(sorted(s)) # much faster than doing str(sorted(s))
            if t not in mp:
                mp[t] = len(result)
                result.append([s])
            else:
                result[mp[t]].append(s)
        return result