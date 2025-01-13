'''
Problem Statement
Design and implement a data structure for Least Recently Used (LRU) Cache.

The cache should support the following operations:

get(key: int) -> int: Retrieve the value of the key if it exists in the cache; otherwise, return -1.
put(key: int, value: int) -> None: Add or update the value of the key. If the cache exceeds its capacity, evict the least recently used item.
Constraints:

The cache should have a fixed capacity.
Operations get and put must run in O(1) time complexity.

Classes
- Node:
    - prev
    - next
    - key
    - value

- LRUCache:
    - capacity
    - key_map: dict[int, Node]
    - lru: Node

    get(key: int) -> str

    put(key: int, value: str) -> str


    _remove_key

    _add_key_to_head

    _move_key_to_head

    -move_key_to_tail
'''

class Node:
    def __init__(self, key: int):
        self.prev = None
        self.next = None
        self.key = key
        self.value = Node(0,0)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.lru = Node(0,0)
        self.head = Node(0,0)
        self.tail = Node(0,0)


# get(key: int) -> int: Retrieve the value of the key if it exists in the cache; otherwise, return -1.
# put(key: int, value: int) -> None: Add or update the value of the key. If the cache exceeds its capacity, evict the least recently used item.
    def get(self, key: int) -> str:

        if key in self.key_map:
            node = self.key_map[key]
            self._move_key_to_head(key)
            return node.value
        return -1

    def put(self, key: int, value: Node) -> None:
        # Update
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._move_key_to_head(node)
        else:
            # add
            node = self.key_map[key]
            self.key_map[key] = Node(key, value)
            self._add_key_to_head(node)

        if len(self.key_map) > self.capacity:
            self._remove_key(self.lru)


    def _add_key_to_head(self, node: Node):
        previous_node = self.head.prev
        next_node = self.head.next
        self.head.prev = node



    def _move_key_to_head(self, node: Node):
        self.head.next.prev = node

        self.head.next = node
    def _remove_key(self, node: Node):
        lru = node
        self._remove_from_tail(lru)

    def _remove_from_tail(self, lru: Node):
        prev = lru.prev
        self.tail.prev = prev
        prev.next = self.tail


'''
Commentary:
Messed up the Node class need to be both key: int, value: int
Messed up LRU Cache class, needs head and tail as dummy values.
- head.next points to tail
- tail.prev points to self.head
Messed up excess capactiy not only need to remove_tail but need to del the key which you get from the return value node of remove_tail
Add_to_node:
- process should be update node first
    - node.prev = self.head
    - node.next = self.head.next
- then update head
    - self.head.next.prev = node
    - self.head.next = node

Remove_node:
- save node prev in variable = node.prev
- save node next in variable = node.next
- prev_node.next = next_node
- next_node.prev = prev_node

Move node to head:
- call remove_node
- call add_node

Remove_tail
- store current tail.prev as lru
call Remove node
return lru node

'''