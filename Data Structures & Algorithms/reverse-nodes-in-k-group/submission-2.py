class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_tail = dummy

        while True:
            kth_node = self.get_kth(prev_tail, k)

            if not kth_node:
                break

            next_head = kth_node.next

            prev = next_head
            curr = prev_tail.next

            while curr != next_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            old_head = prev_tail.next
            prev_tail.next = kth_node
            prev_tail = old_head

        return dummy.next






            
        pass

    def get_kth(self, node, k):
        while node and k:
            node = node.next
            k -= 1

        return node