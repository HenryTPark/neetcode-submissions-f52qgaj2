# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # d 0 1 2 3 4 5 6
        #         s
        #                 f
        # 0 6

        # d 0 1 2 3 4 5
        #       s
        #             f


        # slow fast both start from dummy
        # while fast and fast.next

        # 0 1 2 3
        # 6 5 4
        if not head:
            return None

        dummy_node = ListNode(-1, head)
        slow, fast = dummy_node, dummy_node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head

        second = slow.next
        slow.next = None

        prev_second = None

        while second:
            next_second = second.next

            second.next = prev_second
            prev_second = second
            second = next_second

        second = prev_second


        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first
            
            first = next_first
            second = next_second


        
        