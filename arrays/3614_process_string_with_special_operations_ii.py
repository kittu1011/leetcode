# Original Optimal solution
class Solution:
    def processStr(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch == '*' and size:
                size -= 1
            elif ch == '#':
                size *= 2
            elif ch.isalpha():
                size += 1

        if k >= size:
            return '.'
        for ch in reversed(s):
            if ch == '*' and size:
                size += 1
            elif ch == '#':
                size //= 2
                k %= size
            elif ch == '%':
                k = size - 1 - k                
            elif ch.isalpha():
                size -= 1
                if size == k:
                    return ch
# Optimized solution by comparing ints instead of string objects
class Solution:
    def processStr(self, s: str, k: int) -> str:
        sc = s.encode()
        size = 0
        star = ord('*')
        tag = ord('#')
        mod = ord('%')
        a = ord('a')

        for ch in sc:
            if ch == star and size:
                size -= 1
            elif ch == tag:
                size *= 2
            elif ch >= a:
                size += 1

        if k >= size:
            return '.'
        
        for ch in reversed(sc):
            if ch == star:
                size += 1
            elif ch == tag:
                size >>= 1
                k %= size
            elif ch == mod:
                k = size - 1 - k                
            elif ch >= a:
                size -= 1
                if size == k:
                    return chr(ch)