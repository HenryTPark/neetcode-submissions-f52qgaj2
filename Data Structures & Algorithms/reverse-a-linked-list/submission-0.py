# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) Time | O(1) Space
        prev = None
        node = head

        while node:
            next_node = node.next

            node.next = prev
            prev = node
            node = next_node
        
        return prev
        