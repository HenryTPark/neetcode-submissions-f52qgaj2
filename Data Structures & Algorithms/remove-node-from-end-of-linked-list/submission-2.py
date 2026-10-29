# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # d 1 2 | 2
        # s   f
        # 
        
        # d 1 2 3 4 | n = 2
        #     s   f

        dummy_node = ListNode(-1, head)

        slow, fast = dummy_node, dummy_node

        while fast and n:
            fast = fast.next
            n -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_node.next
        


        
        