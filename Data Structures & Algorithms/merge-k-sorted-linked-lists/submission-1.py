# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_lists(list1, list2):
            dummy_node = ListNode(-1)
            node = dummy_node

            while list1 and list2:
                val1 = list1.val
                val2 = list2.val
                
                if val1 < val2:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next

                node = node.next
            
            if list1:
                node.next = list1
            elif list2:
                node.next = list2
            
            return dummy_node.next

        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge_lists(lists[i], lists[i + interval])

            interval *= 2


        return lists[0]
        