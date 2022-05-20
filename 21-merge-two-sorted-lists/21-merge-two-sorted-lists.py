# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            if list1 == None:
                return list2
            else:
                return list1
        else:
            if list1.val >= list2.val:
                temp1 = self.mergeTwoLists(list1,list2.next)
                list2.next = temp1
                return list2
            else:
                temp1 = self.mergeTwoLists(list1.next,list2)
                list1.next = temp1
                return list1
                