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

        while len(lists) > 1:
            n = len(lists)
            new_lists = []

            for i in range(0, n, 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < n else None

                new_lists.append(merge_lists(list1, list2))

            lists = new_lists

        return lists[0]
        