# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case = 0

        # recursive case look for the min of left and right

        if not root: 
            return 0
        
        que = deque([(root, 1)])
        while que: 
            node, level = que.popleft()
            if not node.left and not node.right: 
                return level 
            if node.left: 
                que.append((node.left, level + 1))
            if node.right: 
                que.append((node.right, level + 1))
        return level