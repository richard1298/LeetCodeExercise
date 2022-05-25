# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_helper(root):
            if root is not None:
                temp = root.left
                root.left = root.right
                root.right = temp
                swap_helper(root.left)
                swap_helper(root.right)
            else:
                return
        swap_helper(root)
        return root