# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr == None:
            return None
        elif curr.next == None:
            return curr
        else:          
            nxt = curr.next
            prev = None
            curr.next = None
            #print('current node =',curr)
            #print('next node =',nxt)
            while nxt!= None:
                #print('prev node=',prev)
                prev = curr
                #print('updated prev node=',prev)
                #print('curr  node=',curr)
                curr = nxt
                #print('updated curr node=',curr)
                #print('next node =',nxt)
                nxt = curr.next
                #print('updated next node=',nxt)
                curr.next = prev        
        return curr