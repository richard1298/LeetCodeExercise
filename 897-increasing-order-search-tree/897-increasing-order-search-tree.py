# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = []
        def orderflip(root):
            if root is None:
                return
            else:
                orderflip(root.left)
                self.ans.append(root.val)
                orderflip(root.right)
        orderflip(root)
        nodelist = [TreeNode(i,left=None,right=None) for i in self.ans]
        for i in range(len(self.ans)-1):
            nodelist[i].right = nodelist[i+1]
        return nodelist[0]
            
            
                
            