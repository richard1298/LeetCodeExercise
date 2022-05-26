# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.target = root.val
        self.result = True
        def dfs_helper(root):
            if root is not None:
                if root.val == self.target:
                    dfs_helper(root.left)
                    dfs_helper(root.right)
                else:
                    self.result = False
        dfs_helper(root)
        return self.result