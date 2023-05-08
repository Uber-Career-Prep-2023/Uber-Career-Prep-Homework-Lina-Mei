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
    def delete(self, val): 
        """ 
        :type self : BinarySearchTree
        :type val : int
        :rtype : void
        """
        if self == None:
            return self
        if val < self.left.val:
            return self.left.delete(val)
        elif val > self.right.val:
            return self.right.delete(val)
        else:
            
            # When there is no child / 1 child
            if self.left is None:
                temp = self.right
                self = None
                return temp
    
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # when there are two children
            temp = min(self.right)
            self.val = temp.val
            self.right = self.right.delete(temp.val)
            
        return self

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

    print(BST.min())
    print(BST.max())
    print(BST.contains(30)) # true
    print(BST.contains(0)) # false
    
main()