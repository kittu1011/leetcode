# Original Optimal Solution
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        ten = {str(i) for i in range(1,10)}
        empts = []
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empts.append((i,j))
                    continue
                s = (i // 3) * 3 + (j // 3)
                rows[i].add(ch)
                cols[j].add(ch)
                sqrs[s].add(ch)
        
        def helper(idx):
            if idx == len(empts):
                return True
            
            i,j = empts[idx]
            ch = board[i][j]
           
            s = (i // 3) * 3 + (j // 3)
            nums = ten - (rows[i] | cols[j] | sqrs[s])

            if not nums:
                return False
            
            for num in nums:
                rows[i].add(num)
                cols[j].add(num)
                sqrs[s].add(num)
                board[i][j] = num
                if helper(idx + 1) == True:
                    return True
                rows[i].remove(num)
                cols[j].remove(num)
                sqrs[s].remove(num)
                board[i][j] = '.'
            return False
        
        helper(0)