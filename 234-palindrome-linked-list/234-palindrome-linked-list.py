# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = head
        lst = []
        while s:
            lst.append(s.val)
            s = s.next
        #print(lst)
        return lst == lst[-1::-1]
            
        