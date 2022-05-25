"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depth_helper(root):
            result = 0
            if root is not None:
                result = 1
                if root.children != []:
                    child_list = root.children
                    for elem in child_list:
                        temp = depth_helper(elem)
                        result = max(result,1+temp)
            return result
        return depth_helper(root)