# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) Time | O(1) Space
        dummy_node = ListNode(-1)
        node = dummy_node

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 < val2:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next
        
        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy_node.next
        