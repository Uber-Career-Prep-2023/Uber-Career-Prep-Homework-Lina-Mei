""" 
In each of the methods, use pointers in languages that support pointers (e.g., Node * in C++) or  
references in languages that support references (e.g., Python). Your Node struct will be the same 
as for your doubly linked list except the two pointers/references should be left and right rather 
than next and prev. Note that the delete method is more difficult than the insert method; you won’t 
need it for the rest of the assignment so either stop or get help from your mentor if you are stuck after 40 minutes.

Time Complexity: O(N) for insertion, deletion, contains where N is the number of elements in the tree
Space Complexity: O(N) where N is the number of elements in the tree

~ 1 hour total

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # returns the minimum value in the BST
    def min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val
        
    # returns the maximum value in the BST
    def max(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val
    
    # returns a boolean indicating whether val is present in the BST
    def contains(self, val):
        """ 
        :type self : BinarySearchTree
        :type val : int
        :rtype : bool
        """
        curr = self
        while curr:
            if val == curr.val:
                return True
            elif val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return False
        
    # For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    # creates a new Node with data val in the appropriate location
    def insert(self, val):
        if self is None:
            return Node(val)
        if self.val == val:
            return self
        elif self.val > val:
            if not self.left:
                self.left = BinarySearchTree(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BinarySearchTree(val)
            else:
                self.right.insert(val)
        return self
            
        
    # deletes the Node with data val, if it exists
    def delete(root, val):
        # Base Case
        if root is None:
            return root
    
        if val < root.val:
            root.left = root.left.delete(val)
    
        elif(val > root.val):
            root.right = root.right.delete(val)
    
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = min(root.right)
    
            # Copy the inorder successor's
            # content to this node
            root.key = temp.key
    
            # Delete the inorder successor
            root.right = root.right.delete(temp.key)
    
        return root

def main():
    # Driver code from geeksforgeeks
    """ Let us create following BST
                50
            /     \
            30      70
            /  \    /  \
        20   40  60   80 """
        
    BST = BinarySearchTree(50)
    BST.insert(30)
    BST.insert(20)
    BST.insert(40)
    BST.insert(70)
    BST.insert(60)
    BST.insert(80)

    print(BST.min()) # 20
    print(BST.max()) # 80
    
    BST.delete(80)
    print(BST.max()) # 70

    
    print(BST.contains(30)) # true
    print(BST.contains(0)) # false
    
main()