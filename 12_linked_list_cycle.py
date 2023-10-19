'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        try: 
            slow = head 
            fast = head.next 
            while slow is not fast: 
                slow = slow.next 
                fast = fast.next.next

            return True 
        except: 
            return False

            
if __name__=='__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next= ListNode(-4)
    self = Solution()
    print(self.hasCycle(head=head))

    '''
    Need to run it in the leetcode console because it will have the internal
    pos number of the next value

    This type of algorithm is the tortoise and the hare algorithm. 
    Slow checks the curent index, fast checks the next index, so if it
    does cycle back around and slow == fast it will return true. If it 
    doesn't cycle it will hit an exception and return false. 
    https://leetcode.com/problems/linked-list-cycle/solutions/44494/except-ionally-fast-python/

    Interesting learnings about algorithms: 
    https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare

    Really good leet code solver: Stefan Pochmann: https://leetcode.com/StefanPochmann/
    '''