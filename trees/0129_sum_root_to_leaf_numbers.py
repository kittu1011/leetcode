# Original Recursive Solution
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        def helper(node, curr_sum):
            nonlocal result
            if not node:
                return
            
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                result += curr_sum
                return
            
            helper(node.left, curr_sum)
            helper(node.right, curr_sum)
        
        helper(root,0)
        return result
# Original DFS Solution
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        stk = []
        curr = root
        curr_sum = 0
        while curr or stk:
            if curr:
                curr_sum = curr_sum * 10 + curr.val
                if not curr.left and not curr.right:
                    result += curr_sum
                else:
                    stk.append((curr,curr_sum))
                curr = curr.left
            else:
                curr, curr_sum = stk.pop()
                curr = curr.right
        return result
# Original BFS Solution
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        q = deque()
        q.append((root,0))
        curr = root
        curr_sum = 0
        while q:
            size = len(q)
            for i in range(size):
                curr, curr_sum = q.popleft()
                curr_sum = curr_sum * 10 + curr.val
                if not curr.left and not curr.right:
                    result += curr_sum
                    continue
                if curr.left:
                    q.append((curr.left, curr_sum))
                if curr.right:
                    q.append((curr.right, curr_sum))

        return result