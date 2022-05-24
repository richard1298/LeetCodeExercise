"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        def preorder_helper(root):
            if root is not None:
                self.result.append(root.val)
                if root.children != []:
                    children_list = root.children
                    for elem in children_list:
                        preorder_helper(elem)
        preorder_helper(root)
        return self.result
                    