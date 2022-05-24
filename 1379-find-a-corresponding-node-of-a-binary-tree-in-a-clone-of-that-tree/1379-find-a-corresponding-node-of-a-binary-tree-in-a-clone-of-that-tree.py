# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = None
        def Traverse(o,c):
            if o is not None:
                Traverse(o.left,c.left)
                if o == target:
                    self.result = c
                else:
                    Traverse(o.right,c.right)
        Traverse(original,cloned)
        return self.result
            
            