# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        node = dummy

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 < val2:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next

            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2

        return dummy.next
        
        
        