# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.rep = {}
        self.result = False
        self.target = k
        def find_helper(root,counter=0):
            if root is not None:
                if self.target-root.val in self.rep:
                    self.result = True
                else:
                    self.rep[root.val] = counter
                    find_helper(root.left,counter+1)
                    find_helper(root.right,counter+2)
        find_helper(root,0)
        return self.result