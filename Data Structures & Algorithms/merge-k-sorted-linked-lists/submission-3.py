# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(one, two):
            dummy = ListNode(-1)
            node = dummy

            while one and two:
                val1, val2 = one.val, two.val

                if val1 < val2:
                    node.next = one
                    one = one.next
                else:
                    node.next = two
                    two = two.next

                node = node.next
            
            if one:
                node.next = one
            else:
                node.next = two

            return dummy.next

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            
            interval *= 2


        return lists[0]
        