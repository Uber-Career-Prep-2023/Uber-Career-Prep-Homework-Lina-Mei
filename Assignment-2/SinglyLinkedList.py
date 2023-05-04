class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    # creates new Node with data val at front; returns new head 
    def insertAtFront(self, val):
        """ 
        :type self : Node
        :type val : int
        :rtype : Node
        """
        x = Node(val)
        x.next = self.head
        
        return x
    
    # creates new Node with data val at end
    def insertAtBack(self, val) :
        """ 
        :type self : Node
        :type val : int
        :rtype : Node
        """
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = Node(val)
        
    # creates new Node with data val after Node loc
    def insertAfter(self, val, loc):
        """ 
        :type head : Node
        :type val : int
        :type loc : Node
        :rtype : Node
        """
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = Node(val)

    def deleteFront(self):
        """ 
        :type head : Node
        :rtype : Node
        """
        #removes first Node; returns new head
        x = None
        if self.head:
            x = self.head.next
            self.head.next = None
            self.head = None
        return x

    def deleteBack(head):
        """ 
        :type head : Node
        """
        #removes last Node
        return

    def deleteNode(head, loc):
        """ 
        :type head : Node
        :type loc : Node
        :rtype : Node
        """
        #deletes Node loc; returns head
        return

    def length(head):
        """ 
        :type head : Node
        :rtype : Int
        """
        #returns length of the list
        return 0

    def reverseIterative(head):
        """ 
        :type head : Node
        """
        #reverses the linked list iteratively
        return

    def reverseRecursive(head):
        """ 
        :type head : Node
        """
        #reverses the linked list recursively (Hint: you will need a helper function)
        return
            
        
"""
"""