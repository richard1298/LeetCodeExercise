# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        n = 0
        this = head
        while this!=None:
            result = 2*result+this.val
            this = this.next
        return result