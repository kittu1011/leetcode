# Original Optimal Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue
                sqr_idx = (i // 3) * 3 + (j // 3)
                if ch in rows[i] or ch in cols[j] or ch in sqrs[sqr_idx]:
                    return False
                rows[i].add(ch)
                cols[j].add(ch)
                sqrs[sqr_idx].add(ch)
        
        return True