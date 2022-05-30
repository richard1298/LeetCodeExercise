# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ret = float('inf')
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    result.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        result.sort()
        #print('result =',result)
        for j in range(len(result)-1):
            temp = abs(result[j]-result[j+1])
            ret = min(temp,ret)
        return ret
        
                    
            