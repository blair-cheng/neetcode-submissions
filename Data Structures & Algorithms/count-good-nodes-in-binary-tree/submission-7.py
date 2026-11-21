# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node,mx):
            nonlocal res
            if not node:
                return 0
            if node.val >= mx:
                res += 1
                mx = node.val
            dfs(node.left, mx)
            dfs(node.right, mx)


        dfs(root, root.val)
        return res
        