# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''

d 1 2 3 4
    s
        f

d 5
s
  f

while fast.next

'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(N) Time | O(1) Space
        if not head:
            return None

        dummy_node = ListNode(-1, head)

        slow, fast = dummy_node, dummy_node

        while fast and n:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy_node.next
