'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support
 all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


'''

class MyQueue(object):

    def __init__(self):
        self.push_stk = []
        self.pop_stk = []
        
    # Push element x to the back of queue
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stk.append(x)

        
    # Remove the element from the front of the queue and returns it
    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.pop_stk.pop()

    # Get the front element
    def peek(self):
        """
        :rtype: int
        """
        if not self.pop_stk: 
            while self.push_stk: 
                self.pop_stk.append(self.push_stk.pop())

        return self.pop_stk[-1]

    # Return whether the queue is empty
    def empty(self):
        """
        :rtype: bool
        """
        return not self.push_stk and not self.pop_stk
        


# Your MyQueue object will be instantiated and called as such:
if __name__=='__main__':
    obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()


    '''
    https://www.youtube.com/watch?v=rW4vm0-DLYc



    Stack: 
    Last in first Out (LIFO): 
    - Append to the end fo the list, remove the last appended value 
    --> adding = pushing
    --> removing == popping
    --> top = value just added 
    Implement with queue: 
    Queue: A queue is a data structure that is a line (FIFO: first in first out)
    - not efficient to implement a queue with a stack but it can be done
    - To do this instead of getting the value in a queue you pop the first n-1
    values then add them to the end fo the queue until you get what is now
    the first value. 
    you can do this with just 1 queue instead of 2. 

    
    Below is for problem 225
    You can push values in O(1) but can only pop values in O(n) time
    because n is the current size of the queue
    

    deque: double ended queue in python but we can just use it as a 
    normal queue
    popleft: where you are allowed to pop from in a queue (deque())
    - this is the python method to do that
    You can combine this with the push method which is just appending
    to make one line of self.push(self.q.popleft())
    The retunr the popped last value.


    Don't use Queue vs Dequeue because Queue is a synchornized queue class for 
    multithreaded programming. you can get away with it on LeetCode 
    but it's not recommended for use as a general data structure because there's 
    overhead for the synchronization
    '''