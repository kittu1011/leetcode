# Original Recursive solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxi: int):
            if not root:
                return 0
            
            maxi = max(maxi,root.val)
            return int(root.val >= maxi) + helper(root.left,maxi) + helper(root.right,maxi)

        return helper(root,-1e5)
# Original DFS solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        curr = root
        maxi = root.val
        stk = []

        while stk or curr:
            if curr:
                maxi = max(curr.val, maxi)
                if curr.val == maxi:
                    result += 1
                stk.append((curr,maxi))
                curr = curr.left
            else:
                curr, maxi = stk.pop()
                curr = curr.right
        
        return result
# Original BFS solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        curr = root
        maxi = root.val
        q = collections.deque()
        q.append((curr,maxi))

        while q:
            size = len(q)
            for _ in range(size):
                curr, maxi = q.popleft()
                maxi = max(curr.val,maxi)
                if curr.val == maxi:
                    result += 1
                if curr.left:
                    q.append((curr.left,maxi))
                if curr.right:
                    q.append((curr.right,maxi))

        return result