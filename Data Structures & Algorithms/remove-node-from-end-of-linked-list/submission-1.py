# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # d 1 2 3 4
        #     s     f

        # 1 2 3 4
        #     s   f
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = head

        while fast and n:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
            
        