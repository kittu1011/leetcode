#Original Optimal Solution
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        rows = [0] * r
        cols = [0] * c
        result = 0
        for row in range(r):
            for col in range(c):
                result += grid[row][col]
                rows[row] += grid[row][col]
                cols[col] += grid[row][col]

        for row in range(len(grid)):
            if rows[row] != 1:
                continue
            for col in range(len(cols)):
                if cols[col] != 1:
                    continue
                if grid[row][col] == 1:
                    result -= 1       
        return result