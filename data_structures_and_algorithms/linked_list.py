'''
A linked list is a linear data structure 
in which the elements are not stored at 
contiguous memory locations. 
The elements in a linked list are linked using pointers


Head --> data next --> data next --> data next --> Null
            NODE          NODE          NODE


            A linked list consists of nodes where each 
            node contains a data field and a reference(link)
            to the next node in the list 


Node structure: A node in a linked list 
typically consists of two components

Data: it holds the actual value or data associated with 
the node

Next Points: it stores the memory address (reference)
of the next node in the sequence

Head and Tail: The linked list is accessed through 
the head node, which points to the first node in the list 
The last node in the list points to Null or nullptr, indicating 
the end of the list 
This node is known as the tail node. 

Why linked list data structure needed? 
1) Dynatmic data structure: the size of memory can be allocated or de-allocated
at run time based on the oprtation insertion or deletion
2) Ease of Insertion/Deletion: the insetion and deletion of elements are 
simpler than arrays since no elements need to be shifted after insertion 
and deletion. Just the address needed to be updated. 
3) Efficient Memory Utilization: As we know linked list is a dynamic data structure
the size increases or decreases as per the requirement so this avoids the 
wastage of memory. 
4) Implementation: Various advanced data structures can be implemeted 
using a linked list like a stack, queue, graph, hashmaps. 


3 Types of Linked Lists:
1) Single Linked List 
    - Each node contains a reference to the next node in the sequence. 
    - Traversing a singly linked list done in a forward direction
2) double linked list 
    - In a doubly linked list, each node contains references to both the 
    next and previous nodes. This allows for traversal in both forward 
    and backward directions, but it requires additional memory for the backward
    reference 

    Head --> prev data next --> prev data next -> prev data next --> Null
    Null <-- prev data next <-- prev data next <-- prev data next
3) circular linked list 

    - In a circular linked list, the last node points back to the head node, 
    creating a circular stricture. It can be either singly or doubly linked

    Head --> data next --> data next --> data next --
    ^------------------------------------------------

Operations on Linked List: 
1) Insertion: Adding a new node to a linked list involves adjusting the 
pointers of the existing nodes to maintain the proper sequence. Insertion
can be performed at the beginning, end, or any position within the list
2) Deletion: Removing a node from a linked list requires adjusting the pointers
of the neighboring nodes to bridge the gap left by the deleted node. 
Deletion can be performed at the beginning, end, or any position within 
the list.
3) Searching: searching for a specific value in a linked list involves 
traversing the list from the head node until the value is found or the end
of the list is reached




'''