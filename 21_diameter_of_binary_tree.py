# 543

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # First attempt: Doesn't pass all test cases 100/105
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base case 
        if not root: 
            return 0 
        
        root_left = root.left
        left_path_length = 1 + self.longestPath(root.left)

        root_right = root.right
        right_path_length = 1 + self.longestPath(root.right)
        return left_path_length + right_path_length

    def longestPath(self, root: Optional[TreeNode]):

        if not root: 
            return 0
        return 1 + max(self.longestPath(root.left), self.longestPath(root.right))

    




'''

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


'''