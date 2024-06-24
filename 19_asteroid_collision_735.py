from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


'''
Explanation:
Initialization:

We start with an empty stack.
Iterate through Asteroids:

For each asteroid in the list:

If the stack is empty or the asteroid is moving right (asteroid >

0), append it to the stack.

If the asteroid is moving left (asteroid < 0):

While the stack is not empty and the top of the stack is a
right-moving asteroid (stack[-1] > 0), handle the collision.
If the current asteroid is larger in absolute value, it destroys
 the top of the stack (stack.pop()) and we continue checking for
more collisions.

If the current asteroid is equal in size to the top of the stack,
both asteroids destroy each other (stack.pop()) and we stop
checking further.

If the current asteroid is smaller in absolute value, it gets
destroyed, and we stop checking further.

Result:

The stack contains the state of the asteroids after all collisions.

Time Complexity:

O(N), where N is the number of asteroids. Each asteroid is pushed
and popped from the stack at most once.
Space Complexity:

O(N), for the stack storing asteroids.
'''