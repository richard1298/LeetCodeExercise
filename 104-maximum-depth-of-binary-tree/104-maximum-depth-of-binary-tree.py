# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs_helper(root):
            if root is not None:
                return 1+max(dfs_helper(root.left),dfs_helper(root.right))
            else:
                return 0
        return dfs_helper(root)
            
        