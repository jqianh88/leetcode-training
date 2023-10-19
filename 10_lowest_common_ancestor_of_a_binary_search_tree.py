'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q 
as descendants (where we allow a node to be a descendant of itself).

Inputs: 
- root: list
- p: int
- q: int

Outputs: 
- LCA: int
'''



class TreeNode(object):
    def __init__(self, x): 
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        while True: 
            if root.val > p.val and root.val > q.val: 
                root = root.left 
            elif root.val < p.val and root.val < q.val: 
                root = root.right
            else: 
                return root


if __name__=='__main__':
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 8

    root = TreeNode(x=6)
    root.left = TreeNode(x=2)
    root.right = TreeNode(x=8)
    root.left.left = TreeNode(x=0)
    root.left.right = TreeNode(x=4)
    root.left.right.left = TreeNode(x=3)
    root.left.right.right = TreeNode(x=5)
    root.left.left.left = TreeNode(x=None)
    root.left.left.right = TreeNode(x=None)
    root.right.left = TreeNode(x=7)
    root.right.right = TreeNode(x=9)
    p = TreeNode(x=p)
    q = TreeNode(x=q)
    self = Solution()
    print(self.lowestCommonAncestor(root=root, p=p, q=q))


    '''
    Learnings: 
    We will rely upon the invariant of the BST to solve the exercise. 
    We know that the left subtree of each node contains nodes with smaller
    values and the right subtree contains nodes with greater values.
    We also know that if two nodes, x and y, are on different
    subtrees of a node z (one in the left portion and one in the right portion), 
    then x and y have z as the lowest common ancestor. 
    Having these facts in mind, a possible solution looks like the following:
    
    '''