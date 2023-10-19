'''
Cliimbing Stairs 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct
 ways can you climb to the top?

Steps to think about this: 
1) View it as a decision tree
2) see the patterns in the decision tree 
3) see that the last two steps are 1 and 1, 
for every case. 
So that means we can go from back to front
and just add the previous two steps (one and two)
4) two is the furthest step, one is the penultimate step
5) REturn one after updating one and two as you go.
 
two = 1
one = 1
next = 2
next.next = 3
next.next.next = 5
Beats 98.28% for Time 
Beats 92.16% for memory
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1 
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp 
            
        return one



if __name__=='__main__':
    self = Solution()
    n = 5
    print(self.climbStairs(n=n))