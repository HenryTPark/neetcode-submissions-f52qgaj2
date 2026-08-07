"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''

        3 7 4 5 N

        create copy next to node

        3 3' 7 7' 4 4' 5 5' N

        point the randoms

        separate copies with original
        
        3 7 4 5 N
        
        3' 7' 4' 5' N
        
        '''
        if not head:
            return head

        node = head
        
        while node:
            next_node = node.next
            copy_node = Node(node.val)

            node.next = copy_node
            copy_node.next = next_node

            node = next_node

        node = head

        while node and node.next:
            next_node = node.next.next

            copy_node = node.next
            copy_node.random = node.random.next if node.random else None
            
            node = next_node
            
        node = head
        copy_head = head.next

        while node and node.next:
            next_node = node.next.next
            copy_node = node.next

            node.next = next_node
            copy_node.next = next_node.next if next_node else None

            node = node.next

        return copy_head


            
            

        
        
        
        