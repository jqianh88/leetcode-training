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
    - prev: Nonde
    - next: None

- LFUCache
    - capacity: int
    - key_map: dict[int, Node]
    - head: Node(0,0)
    - tail: Node(0,0)
    - head.next = tail
    - tail.prev = head

    get(key: int)
    put(key:int)

    _add_to_tail
    _switch_positions
    _move_position
    _remove_tail
    _remove_node

'''
class Node:
    def __init__(self, key: int, value: int, freq: int = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int):
        if key in self.key_map:
            node = self.key_map[key]
            self._move_position(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            node.freq += 1
            self._move_position(node)
        else:
            node = Node(key, value, freq=1)
            self.key_map[key] = node
            self._add_to_tail(node)
            self._move_position(node)
        if len(self.key_map) > self.capacity:
            self._remove_tail()


    def _add_to_tail(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.next = self.tail

    def _switch_positions(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        node.next = prev_node
        node.prev = prev_node.prev
        next_node.prev = prev_node

    def _move_position(self, node: Node):
        # While there are ties keep moving to the front

        while node.prev and node.freq == node.prev.freq:
            self._switch_positions(node)


    def _remove_tail(self) -> Node:
        lfu = self.tail.prev
        self._remove_node(lfu)
        del self.key_map[lfu.key]


    def _remove_node(self, node: Node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node


if __name__ == '__main__':
    pass

    # Example
    lfu = LFUCache(2)
    lfu.put(1, 1)        # Cache: {1=1}
    lfu.put(2, 2)        # Cache: {1=1, 2=2}
    print(lfu.get(1))    # Output: 1 (Cache: {2=2, 1=1})
    lfu.put(3, 3)        # Evicts key 2 (Cache: {1=1, 3=3})
    print(lfu.get(2))    # Output: -1 (not found)
    print(lfu.get(3))    # Output: 3 (Cache: {1=1, 3=3})
    lfu.put(4, 4)        # Evicts key 1 (Cache: {4=4, 3=3})
    print(lfu.get(1))    # Output: -1 (not found)
    print(lfu.get(3))    # Output: 3 (Cache: {4=4, 3=3})
    print(lfu.get(4))    # Output: 4 (Cache: {3=3, 4=4})