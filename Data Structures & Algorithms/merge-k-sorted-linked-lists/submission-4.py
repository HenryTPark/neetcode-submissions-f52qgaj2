# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge_two_lists(list1, list2):
            node1, node2 = list1, list2
            dummy = ListNode(-1)
            node = dummy

            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                
                node = node.next

            if not node1:
                node.next = node2
            else:
                node.next = node1
            
            return dummy.next
        
        offset = 1

        while offset < len(lists):
            for i in range(0, len(lists) - offset, offset * 2):
                lists[i] = merge_two_lists(lists[i], lists[i + offset])
            
            offset *= 2

        return lists[0]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        