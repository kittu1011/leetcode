# Recursive Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        
        helper(root)
        return result

# Optimal iterative DFS
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        stk = []
        while (curr or stk):
            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                top = stk.pop()
                result.append(top.val)
                curr = top.right
        
        return result



