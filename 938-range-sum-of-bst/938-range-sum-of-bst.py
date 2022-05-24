# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        def recur_helper(root,low,high):
            if root is not None:
                recur_helper(root.left,low,high)
                if (root.val <= high) and (root.val >= low):
                    #print('root value =',root.val)
                    self.result += root.val
                    #print('result =',self.result)
                recur_helper(root.right,low,high)
        recur_helper(root,low,high)
        return self.result
                