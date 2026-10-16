# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,l1)
        round = 0
        while l1:
            if l2 != None:
                sum = l1.val + l2.val + round
            else:
                sum = l1.val + round
            l1.val = sum % 10
            if sum >= 10:
                round = 1
            else:
                round = 0
            if l1.next == None and l2 != None and l2.next != None:
                l1.next = l2.next
                l2.next = None
            elif l1.next == None and round == 1:
                l1.next = ListNode(0,None)

            l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return dummy.next

        