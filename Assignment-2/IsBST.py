""" 
Given a binary tree, determine if it is a binary search tree.

Time Complexity:
Space Complexity:
"""

from BinarySearchTrees import *

def IsBst(root):
    if root is None:
        return True
    if root.left:
        if root.left.val > root.val:
            return False
        IsBst(root.left)
    if root.right:
        if root.right.val < root.val:
            return False
        IsBst(root.right)
    return True


def main():
    bst = BinarySearchTree(5)
    bst.insert(2)
    bst.insert(7)
    print(str(IsBst(bst))) # true
    bst.delete(7)
    bst.right = Node(2)
    print(str(IsBst(bst))) # false

    return
main()