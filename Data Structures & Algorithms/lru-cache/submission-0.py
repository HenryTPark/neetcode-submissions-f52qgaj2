class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:
    '''
    doubly linked list to keep track of the most recent (tail) and least recent (head)

    map for key to node
    '''

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node, nxt_node = node.prev, node.nxt

        prev_node.nxt = nxt_node
        nxt_node.prev = prev_node

    def _insert(self, node):
        second_last, last = self.tail.prev, self.tail
        
        second_last.nxt = node
        node.prev = second_last

        last.prev = node
        node.nxt = last
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key]
            self._remove(node)
        
        new_node = Node(key, value)

        self._insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru = self.cache[self.head.nxt.key]

            self._remove(lru)
            del self.cache[lru.key]
