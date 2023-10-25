'''
Heaps: 
- A heap is a tree-based data structures that usually comes 
in two varieties: 
1) Max-heaps where the value in any node is greater than 
all the values in it's child nodes and 
2) Min-heaps where the value in any node is less than all 
of the values in it's child nodes 


How Heaps Work: 
1) Min-heaps: 
The elements are all smaller than their chidlren so the 
root node will be the very smallest element and then 
looking down the tree down the heap the elements get 
bigger and bigger and bigger. 
So that's the basics of what a hepa is but the how do 
we actually create and maintain such a data structure?

a) Insertion: 
When we insert an element it always goes in the next 
empty spot looking top to bottom left to right 

If the insertion is not actually where it should be?
- insert the element there and then bubble it up until 
we get to the righ tspot. So we take the inserted element, 
we compare it until we get to the right spot. So we 
take the inserted element, compare it, with its parent, if 
it's out of order, swap them and then keep going up the 
treein this process. 

What about removing a minimum element? 
- We know the minimum element will always be the root 
node and so that's easy to find but then if we want 
to remove it we might have an empty spot. 
--> So remove the min element there so take out the root
and then we swap that value at the root with the last 
element added. And then of course we swap that value at
the root with the last element added. And the of course
that element might not be in the right spot, so we take 
the root element and bubble it down to the next spot so 
we compare the root with its children, its left it down 
to the next spot so we compare the root with its children
its left child and its right child, and then swap it with
the smaller of the two. And then we keep going down the tree 
until the heap property is restored. So that's how a 
heap operates.

Implementation: 
You'd think a simple class node of a left node and right node 
BUT THERE'S a BETTER WAY

Notice insertions happen at a very particular spot 
so there aren't going to be any gaps in the heap so 
we can use an ARRAY instead to store these values 
and that makes it very compact. And a simple 
equation can map from an index to its left child, 
its right child or to its parent. And so we can 
still get to a left and right child but we don't need to 
have this overhead of a node class





2) Max-heaps: reverse of min heaps
'''


# Implementation of Min Heap

class MinIntHeap(object):
    capacity = 10
    size = 0

    items = [capacity]


    # Helper Methods 
    def get_left_child_index(self, parent_index: int) -> int: 
        return 2 * parent_index + 1
    
    def get_right_child_index(self, parent_index: int) -> int: 
        return 2 * parent_index + 2
    
    def get_parent_index(self, child_index: int) -> int: 
        return (child_index - 1) / 2
    

    def has_left_child(self, index: int) -> bool: 
        return self.get_left_child_index(index) < self.size
   
    def has_right_child(self, index: bool) -> bool: 
        return self.get_right_child_index(index) < self.size
   
    def has_parent(self, index: bool) -> bool: 
        return self.get_parent_index(index) >= 0


    def left_child(self, index: int) -> int: 
        return self.items(self.get_left_child_index(index))
    def right_child(self, index: int) -> int: 
        return self.items(self.get_right_child_index(index))
    def parent(self, index: int) -> int: 
        return self.items(self.get_parent_index(index))

    # Swaps the value of two indices and 
    def swap(self, index_one: int, index_two: int): 
        temp = self.items(index_one)
        self.items(index_one) = self.items(index_two)
        self.items(index_two) = temp

    # Insure extra capacity method 
    def ensure_extra_capacity(self): 
        if self.size == self.capacity:
            # Basics of how an array list operates
            self.items = self.items(capacity * 2)




# Heap Documentation in Python: 
# https://docs.python.org/3/library/heapq.html#:~:text=Heaps%20are%20binary%20trees%20for,are%20considered%20to%20be%20infinite.