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
        head = TreeNode()
        cur_node = head
        for i in range(len(self.ans)):
            new_node = TreeNode(val=self.ans[i])
            cur_node.right = new_node
            cur_node = new_node

        return head.right
                
            
            
                
            