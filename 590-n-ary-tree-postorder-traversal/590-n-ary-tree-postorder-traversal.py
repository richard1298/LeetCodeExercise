"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.result = []
        def postorder_helper(root):
            if root is not None:
                children_list = root.children
                if children_list == []:
                    self.result.append(root.val)
                else:
                    for elem in children_list:
                        postorder_helper(elem)
                    self.result.append(root.val)
        postorder_helper(root)
        return self.result