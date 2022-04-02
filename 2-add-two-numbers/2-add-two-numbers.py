# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#They key here is to understand how linked list work
#1. In this problem, the inputs are two nodes and the list is implicit by traversing through the nodes
#2. No need to worry about the concept of pointer. next attribute simply points to the next ListNode (essentially it could be anything)

        result = ListNode(0)
        pointer = result
        carry = 0
        while l1 or l2 or carry:
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0
            pointer.next = ListNode((first_num + second_num + carry)%10)
            carry = (first_num + second_num + carry)//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pointer = pointer.next
            
        return result.next
            