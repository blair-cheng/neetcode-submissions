# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if node == None:
                return 0

            val = node.val
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(val + left + right , res)
            return val + max(left, right)

        dfs(root)
        return res
        