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

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node) -> None:
        """Add a node right after the dummy head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        """Remove an existing node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_tail(self) -> Node:
        """Remove the tail node and return it."""
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}  # Maps keys to their corresponding nodes
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.dll.remove_node(node)
            self.dll.add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.dll.remove_node(node)
            self.dll.add_to_head(node)
        else:
            if len(self.key_map) >= self.capacity:
                lru_node = self.dll.remove_tail()
                del self.key_map[lru_node.key]
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.dll.add_to_head(new_node)



if __name__ == '__main__':

    cache = LRUCache(capacity=2)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.put(3, 4)
    cache.get(3)
    cache.get(5)



'''
Why Use a DoublyLinkedList Class?
Encapsulation:

Operations like adding to the head, removing nodes, and removing the tail can be isolated in the DoublyLinkedList class, reducing the responsibilities of the LRUCache class.
Code Reusability:

If you need a doubly linked list in other parts of your application (e.g., for another cache type like MRU or LFU), you can reuse the DoublyLinkedList class.
Separation of Concerns:

The LRUCache class focuses on the high-level logic for caching, while the DoublyLinkedList handles low-level operations on nodes.
'''