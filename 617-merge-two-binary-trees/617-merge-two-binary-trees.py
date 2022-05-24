# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_helper(root1,root2):
            #No need to go through every single child nodes of root2
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            root1.val += root2.val
            root1.left = merge_helper(root1.left,root2.left)
            root1.right = merge_helper(root1.right, root2.right)
            return root1
        return merge_helper(root1,root2)
                
                    
                    
                
                
                