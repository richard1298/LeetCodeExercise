# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        result = []
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    result.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        result.sort()
        goal = float('inf')
        for i in range(len(result)-1):
            t = abs(result[i]-result[i+1])
            goal = min(t,goal)
        return goal