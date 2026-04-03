# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
2 4 6 8
  s
    f    

2 4

8 6

2 8 4 6

reverse the latter half

interweave 2 linked lists



[0, 1, 2, 3, 4, 5, 6]
          s
                   f

while fast.next.next is truthy

second_start = slow.next
slow.next = None




[0, 6, 1, 5, 2, 4, 3]

if there are off number of nodes in the original list, we would need to

make the latter half smalelrf


'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow, fast = head, head
        '''
        0 1 2 3 4 5 6
              s
                    f

        '''

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # 4
        slow.next = None


        second_prev = None
        while second:
            second_next = second.next

            second.next = second_prev
            second_prev = second
            second = second_next

        node1 = head
        node2 = second_prev

        while node2:
            next_node1 = node1.next
            next_node2 = node2.next

            node1.next = node2
            node2.next = next_node1

            node1 = next_node1
            node2 = next_node2

        # return head


        