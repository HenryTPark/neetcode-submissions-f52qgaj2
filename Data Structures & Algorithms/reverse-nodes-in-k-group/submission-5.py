# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev_tail = dummy

        def get_kth_node(node, k):
            while node and k:
                node = node.next
                k -= 1
            
            return node

        while True:
            kth_node = get_kth_node(prev_tail, k)

            if not kth_node:
                break

            next_head = kth_node.next # 4

            # 1 2 3 -> 3 2 1

            prev_node = next_head
            node = prev_tail.next

            while node != next_head:
                temp = node.next

                node.next = prev_node
                prev_node = node
                node = temp

            # 3 2 1 4 5 6
            old_head = prev_tail.next
            prev_tail.next = kth_node
            prev_tail = old_head
        
        return dummy.next
        