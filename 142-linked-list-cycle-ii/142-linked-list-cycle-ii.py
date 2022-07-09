# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cycleflag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleflag = True
                break
        if not cycleflag:
            return None
        else:
            slow1 = head
            while slow1 != fast:
                slow1 = slow1.next
                fast = fast.next
        return slow1
            
        