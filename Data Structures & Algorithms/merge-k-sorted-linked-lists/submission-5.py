# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_lists(l1, l2):
            dummy = ListNode(-1)
            node = dummy

            while l1 and l2:
                v1, v2 = l1.val, l2.val

                if v1 < v2:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next

                node = node.next

            if l1:
                node.next = l1
            else:
                node.next = l2

            return dummy.next
        
        offset = 1
        n = len(lists)

        while offset < n:
            for i in range(0, n - offset, offset * 2):
                lists[i] = merge_two_lists(lists[i], lists[i + offset])

            offset *= 2

        return lists[0]
        
        