# Original Optimal solution
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks) # extra memory
        result = n
        i = 0
        white = 0
        for j in range(n):
            if blocks[j] == 'W':
                white += 1
            if j - i + 1 == k:
                result = min(result, white)
                if blocks[i] == 'W':
                    white -= 1
                i += 1
        return result
# Most elegant solution
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[0:k].count('W')
        result = white

        for i in range(k,len(blocks)):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            result = min(result, white)
        return result
