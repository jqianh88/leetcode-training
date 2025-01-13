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
- LRUCache
    - lru: Node
    - capacity: int
    - key_map: {}

    get(key: int)
    put(key: int)


'''
class Node:
    def __init__(self, prev: int):
        self.prev = prev
        self.next = None or int# int

class LRUCache:
    def __init__(self, lru: Node, capacity: int, key_map: dict[str, int]):
        self.lru = lru
        self.capacity = capacity
        self.key_map = key_map

    def get(self, key: int) -> int:
        return self.key_map.get(key) or -1

    def put(self, key: int, value: str) -> None:
        # add or update
        self.key_map[key] = value

        # Evict when the length of the key_map > capacity
        if len(self.key_map) > self.capacity:
            self.key_map[self.lru] = {}
            del self.key_map[self.lru]

        #update the lru
        self.calc_lru()

    # Calculate next lru
    def calc_lru(self):
        self.prev = self.next
        self.next = None
        # not sure how to implement this logic





