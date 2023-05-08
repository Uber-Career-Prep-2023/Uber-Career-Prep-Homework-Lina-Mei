""" 
Given a binary tree, create a deep copy. Return the root of the new tree.
Time Complexity: O(N) where n is the number of nodes in the binary tree
Space Complexity: O(N)

15 minutes taken

Explanation:
    The time complexity is O(N) because the function traverses every node in the tree once and creates a copy of each node.
    The space complexity is O(N) because the function creates a new tree with n nodes
"""

from BinarySearchTrees import BinarySearchTree, Node

def CopyTree(root):
    if not root:
        return None

    copy = Node(root.val)
    copy.left = CopyTree(root.left)
    copy.right = CopyTree(root.right)
    
    return copy

def print_tree(bst):
    if bst:
        print(bst.val)
    if (bst.left):
        print_tree(bst.left)
    if (bst.right):
        print_tree(bst.right)

def main():
    bst = BinarySearchTree(5)
    bst.insert(2)
    bst.insert(7)
    print_tree(bst)
    print(bst)
    bst_copy = CopyTree(bst)
    print_tree(bst_copy)
    print(bst_copy)

    return
    
main()