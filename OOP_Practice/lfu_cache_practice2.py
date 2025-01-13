'''
LFU Cache Problem Statement
Design and implement a data structure for Least Frequently Used (LFU) Cache.

The cache should support the following operations:
    get(key: int) -> int: Retrieve the value of the key if it exists in the cache; otherwise, return -1.
    put(key: int, value: int) -> None: Add or update the value of the key. If the cache reaches its capacity, it should evict the least frequently used item. If there is a tie (multiple keys with the same frequency), evict the least recently used key among them.
    Constraints
    The cache has a fixed capacity.
    Operations get and put must run in O(1) time complexity.

Classes:
- Node:
    - key: int
    - value: int
    - freq: int
    - prev: None
    - next: None

- LFUCache
    - capacity: int
    - key_map: {"key": Node}
    - freq_map: {`freq`: Node}
    - min_freq: int

    get(key: int)
   put(key: int)
   _create_dll
   _evict
   -insert_after_head
   _update_node

'''

class Node:
    def __init__(self, key: int, value: int, freq: int = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class LFUCache:
    def __init__(self, capacity: int, min_freq: int = 1):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {lambda: Node(0,0)}
        self.min_freq = min_freq

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self._update_node(node)
            self._update_freq_map(node)
            return node.value
        return -1

    def put(self, key: int, value: Node):
        if not self.capacity:
            return



        if key not in self.key_map:
            node = Node(key, value)
            self.key_map[key] = node
            self.min_freq = 1
            if node.freq not in self.freq_map:
                self._create_dll(node)
        else:
            node = self.key_map[key]
            self._update_freq_map(node)

        if len(self.key_map) >= self.capacity:
            self._evict(node)

        return node.value


    def _evict(self, node):
        pass

    def _update_node(self, node: Node):
        node.freq += 1

    def _update_freq_map(self, node: Node):
        old_freq = node.freq


    def _create_dll():
        head = Node(0,0)
        tail = Node(0,0)
        head.next = tail
        tail.prev = head
        return head



'''
Trying too hard to memorize the solution rather than deduce it with critical thinking
'''