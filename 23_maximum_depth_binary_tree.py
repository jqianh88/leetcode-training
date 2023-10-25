# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    # Recursive DFS (O(n)) time and space complexity
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        if not root: 
            return 0
        
        level = 0 
        que = deque([root])

        while que: 
            for i in range(len(que)): 
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right: 
                    que.append(node.right)
            level += 1
        return level
    
    # Iterative DFS O(n) time and space
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        if not root: 
            return 0 
        
        node_stack = [[root, 1]]
        response = 1
        while node_stack :
                
            node, depth = node_stack.pop()
            if node:
                response = max(response, depth)
                node_stack.append([node.left, depth + 1])
                node_stack.append([node.right, depth + 1])

        return response

        





"""
This is a tree problem: 

There are at least 3 ways to solve this problem: 
1) Recursive DFS: Depth first search [easiest]
    a) First question: what is the base case: no node --> 0 
    b) Next question: what if there is one node with no children: 
        - 1 + max(left subtree, right subtree)

2) Iterative DFS: Depth first search (without recursion)
    a) You will need a stack data structure because you will be 
    emulating the recursive call stack 
    - Implementation is with Pre-order dfs
        - process node 
        - add left and right node to the stack

    - add node and depth to the stack 
    - Pop and process


3) BFS: Breadth First Search (O(n) time and memory but runs slower)
    - Means we are looking at each level until we can't continue anymore
    Kind of like counting the number of levels we have
    BFS usually requires as queue or deque
    - Initialize the queue with a single value (the root)
    - create a while loop (keep checking until the que is empty)
    - Then For the length of the que you popleft the root at each level
    - replace with the actual numbers of the left and right if they exist 
    - increment the level for each loop
    - return the level




"""