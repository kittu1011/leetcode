# Optimal Solution made with help
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r,t,b = 0, len(matrix)-1, 0, len(matrix)-1
        while l < r:
            for offset in range(r - l):
                temp = matrix[t][l + offset]
                matrix[t][l + offset] = matrix[b - offset][l]
                matrix[b - offset][l] = matrix[b][r - offset]
                matrix[b][r - offset] = matrix[t + offset][r]
                matrix[t + offset][r] = temp
            l += 1
            r -= 1
            t += 1
            b -= 1
         