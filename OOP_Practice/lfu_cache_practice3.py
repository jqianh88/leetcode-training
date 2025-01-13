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

- DoubleLinkedList:
    - head: Node(0,0)
    - tail : Node(0,0)
    - head.next
    - tail.prev

    _add_to_head
    -remove_node
    -remove_tail

- LFUCache:
    - capacity: int
    - key_map: {} key -> Node
    - freq_map: defaultdict(DoubleLinkedList)
    - min_freq

    _update_freq

'''

from collections import defaultdict
class Node:
    def __init__(self, key: int, value: int, freq: int = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head: Node(0,0)
        self.tail: Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        node.prev = node.next        # This should be node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_tail(self, node: Node): #shouldn't need to pass in node
        ### Needed to add check: if self.head.next == self.tail: return None  --> Because the list is empty
        # Should get the tail_node from tail_node = self.tail.prev --> pass it into _remove_node(tail_node) --> return tail_node
        self._remove_node(node)
        return node

class LFUCache:
    def __init__(self, capacity: int, min_freq: int = 1): # should not default min_freq to 1 and should not pass in
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = defaultdict(DoubleLinkedList)
        self.min_freq = min_freq  # Should be set to 0

    def get(self, key: int):
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            # need to update the value --> node.value = value
            self._update_freq(node)

        else:
            if len(self.key_map) >= self.capacity:
                lfu = self.freq_map[self.min_freq]._remove_tail(node) # Shouldn't need to pass in node
                # NEED to delete the node from key_map -->  self.key_map[lfu.key]
                if not self.freq_map[lfu.freq].head.next.next: #don't need this line
                    del self.freq_map[lfu.freq] #don't need this line
            node = Node(key, value)
            # need to add the node to the key_map --> self.key_map[key] = new_node
            node.freq = 1 #don't need this line
            self.freq_map[1]._add_to_head(node)
            # Should set self.min_freq = 1

    def _update_freq(self, node: Node):
        old_freq = node.freq
        self.freq_map[old_freq]._remove_node(node)

        if self.freq_map[old_freq].head.next.next: # Should be a check of self.head.next == self.tail  --> the way it is means that there is somethign which is the opposite of what we want
            del self.freq_map[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq]._add_to_head(node)
