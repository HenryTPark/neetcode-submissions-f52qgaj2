# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(a, b):
            dummy = ListNode(-1)
            node = dummy

            while a and b:
                val1 = a.val
                val2 = b.val

                if val1 < val2:
                    node.next = a
                    a = a.next
                else:
                    node.next = b
                    b = b.next

                node = node.next
            
            if a:
                node.next = a
            else:
                node.next = b

            return dummy.next


        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            
            interval *= 2

        return lists[0]
        
        