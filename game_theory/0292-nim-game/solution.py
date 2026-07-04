class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
# On every multiple on 4 opponent just takes [4 - your move] stones,
# leading you at another multiple of 4 until you hit n = 4 in which you loose