# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            first = list1
            second = list2
            head = list1
        elif list2.val < list1.val:
            first = list2
            second = list1
            head = list2
        
        while first and second:
            temp = first.next
            if temp == None:
                first.next = second
                break
            elif temp.val <= second.val:
                first = first.next
            elif temp.val > second.val:
                first.next = second
                second = temp
        
        return head
        