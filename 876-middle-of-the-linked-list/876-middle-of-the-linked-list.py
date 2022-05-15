# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        rep = {}
        this = head
        while this!= None:
            n += 1
            rep[n] = this
            this = this.next
        return rep[n//2+1]