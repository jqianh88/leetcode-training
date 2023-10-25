# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Iterative: O(n) time and O(1) memory
        # previous, current = None, head

        # while current: 
        #     next = current.next
        #     current.next = prev
        #     prev = current 
        #     current = next

        # return previous
    

        # Recursive: O(n) and O(n)
        if not head: 
            return None
        
        newHead = head 
        if head.next: 
            self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead


if __name__=='__main__':
    # head = [1, 2, 3, 4, 5]
    head =  ListNode(1, 2)
    node2 = ListNode(2, 3)
    node3 = ListNode(3, 4)
    node4 = ListNode(4, 5)
    node5 = ListNode(5, None)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
   
    self = Solution()
    print(self.reverseList(head))

    '''
    The above is how a linked list works
    Each node has a value within that node 
    and points to the next node that has a value
    You must define {node}.next so that you 
    can link this long list together. 

    '''