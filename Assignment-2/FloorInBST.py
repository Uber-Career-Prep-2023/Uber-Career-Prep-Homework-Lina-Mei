""" 
Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.

Time Complexity: O(h) where h is the height of the tree
Space Complexity: O(h) where h is the height of the tree

16 minutes taken total

Explanation:
    The time complexity is O(h) because the algorithm may need to traverse the entire height of the tree to find the floor value
    The space complexity is O(h) because the maximum number of recursive calls on the call stack is equal to the height of the tree
"""
from BinarySearchTrees import *

def FloorInBST(bst: BinarySearchTree, target: int):
    if target == bst.val:
        return bst.val
    if target > bst.val:
        if bst.right:
            return FloorInBST(bst.right, target)
    if target < bst.val:
        if bst.left:
            return FloorInBST(bst.left, target)
    if not bst.right and not bst.left:
        return bst.val

def main():
    bst = BinarySearchTree(10)
    bst.insert(9)
    bst.insert(8)
    bst.insert(16)
    bst.insert(13)
    bst.insert(17)
    bst.insert(20)    
    print(FloorInBST(bst, 13)) # 13
    print(FloorInBST(bst, 15)) # 13

    return
main()