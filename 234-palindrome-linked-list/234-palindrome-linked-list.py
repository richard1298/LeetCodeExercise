# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dic = {}
        idx = 0
        s = head
        while s:
            idx += 1
            dic[idx] = s                
            s = s.next
        l = 1
        r = idx
        flag = True
        while l<= r:
            if dic[l].val == dic[r].val:
                l += 1
                r -= 1
            else:
                flag = False
                break
        return flag
            
        
            
            
        