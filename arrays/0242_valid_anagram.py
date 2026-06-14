# Original Solution optimized for space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = [0] * 26
        freq_t = [0] * 26
        for ch in s:
            freq_s[ord(ch) - ord('a')] += 1
        for ch in t:
            freq_t[ord(ch) - ord('a')] += 1

        return freq_s == freq_t
    
# Solution optimized for space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0: # Since s and t are same length, t will have more of some letter if they are not anagrams
                return False
        return True

 # New take on prior solutions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        return freq == [0] * 26