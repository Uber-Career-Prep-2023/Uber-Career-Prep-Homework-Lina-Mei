""" 
Given a binary tree, determine if it is a binary search tree.

Time Complexity: O(N) where N represents the number of elements in the tree
Space Complexity: O(1)

10 minutes taken total

Explanation:
    The time complexity is O(N) because we have to traverse through all the nodes in the tree
    The space complexity is O(1) because we do not need new space allocation at all
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