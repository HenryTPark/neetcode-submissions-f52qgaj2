class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev_tail = dummy

        while True:
            kth_node = self.get_kth_node(prev_tail, k)

            if not kth_node:
                break

            next_head = kth_node.next

            prev_node = next_head
            curr_node = prev_tail.next

            while curr_node != next_head:
                temp_node = curr_node.next

                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp_node

            # 1 2 3 4 5 6
            # 3 2 1 4 5 6


            old_head = prev_tail.next # 1
            prev_tail.next = kth_node # 3
            prev_tail = old_head # 

        return dummy.next

    def get_kth_node(self, node, k):
        while node and k:
            node = node.next
            k -= 1

        return node