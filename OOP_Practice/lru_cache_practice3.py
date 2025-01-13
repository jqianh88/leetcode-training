'''
Problem Statement
Design and implement a data structure for Least Recently Used (LRU) Cache.

The cache should support the following operations:

get(key: int) -> int: Retrieve the value of the key if it exists in the cache; otherwise, return -1.
put(key: int, value: int) -> None: Add or update the value of the key. If the cache exceeds its capacity, evict the least recently used item.
Constraints:

The cache should have a fixed capacity.
Operations get and put must run in O(1) time complexity.


Classes:
- Node:
    - prev: None
    - next: None
    - key: int
    - value: int

- LRUCache
    - capacity: int
    - key_map: dict[key, Node]
    - head: Node(0,0)
    - tail: Node(0,0)
    - head.next = tail
    - tail.prev = head

    get(key: int)
    put(key: int, value: Node)

    add_to_head(node: Node)
    move_to_head(node: Node)
    remove_node(node: Node)
    remove_tail() -> Node
'''

class Node:
    def __init__(self, key:int, value:int):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: Node) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.key_map[key] = node
            self._add_to_head(node)
        if len(self.key_map) > self.capacity:
            lru = self._remove_tail()
            del self.key_map[lru.key]


    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self) -> Node:
        lru = self.tail.prev
        self._remove_node(lru)
        prev_node = lru.prev
        self.tail.prev = prev_node
        return lru

if __name__ == '__main__':

    cache = LRUCache(capacity=2)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.put(3, 4)
    cache.get(3)
    cache.get(5)
