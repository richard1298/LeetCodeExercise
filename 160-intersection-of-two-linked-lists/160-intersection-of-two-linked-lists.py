# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currB = headB
        rep2 = {}
        i=1
        while currB != None:
            rep2[currB] = i
            i += 1
            currB = currB.next
        result = None
        j = 1
        currA = headA
        while currA != None:
            if currA in rep2:
                result = currA
                break
            else:
                j+=1
                currA = currA.next
        return result
                
                