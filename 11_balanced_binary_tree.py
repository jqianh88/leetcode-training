'''
Given a binary tree, determine if it is height-balanced (
depth of two subtrees of every node never differs by more than 1
).
'''

# Definition for a binary tree node. 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right


class Solution(object):
    def isBalanced(self, root: TreeNode):
        def check(root): 
            if root is None: 
                return 0 
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1 
            return 1 + max(left, right)
        return check(root) != -1
        

if __name__=='__main__':
    root = [3,9,20,None,None,15,7]

    root = TreeNode(val=3)
    root.left = TreeNode(val=9)
    root.right = TreeNode(val=20)
    root.left.left = TreeNode(val=None)
    root.left.right = TreeNode(val=None)
    root.right.left = TreeNode(val=15)
    root.right.right = TreeNode(val=7)
    self = Solution()
    print(self.isBalanced(root=root))

    '''
    Height-Balanced: abs(Height_left - Height_right) <= 1
    which means their difference can be 0 (same height) or 1
    - Check at each node if the leaf node is balanced. 

    This is a Depth first search question.
    Need to check 3 things: 
    1) Left node balanced
    2) Right node should be balanced
    3) Heights of the left and right subtree should be at most 1

    return whether each node is balanced or not and the height of the
    tree 

    Time complexity: O(n) because only have to go through nodes once
    Space complexity O(n) because of the DFS call stack
    '''