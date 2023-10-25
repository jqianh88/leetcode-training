# 876
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        return slow
        
        


'''
This method is called the Two Pointers method. 
Fast goes twice as fast so for both even and odd cases 
when slow reaches the middle or if there are two middle 
nodes the second middle will be where slow is when fast
finishes. 


The of course other easy way to do this would be to 
iterate through the entire linked list and keep track of the
cout then if odd (//2) and if even (//2 + 1).
Then you would need to iterate through the list until 
you got to that node of the linked list, 
'''