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
        self.head = x
        return self.head
    
    # creates new Node with data val at end
    def insertAtBack(self, val) :
        """ 
        :type self : Node
        :type val : int
        :rtype : Node
        """
        if self.head is None:
            self.head = Node(val)
            return
        else:
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
        if self.head is None:
            return
        else:
            curr = self.head
            while curr.next:
                if curr.next == loc:
                    temp = curr.next.next
                    curr.next = None
                    curr.next = temp
                else:
                    curr=curr.next
        
    #removes first Node; returns new head
    def deleteFront(self):
        """ 
        :type head : Node
        :rtype : Node
        """
        if self.head is None:
            return
        else:
            x = None
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        return self.head
    
    #removes last Node
    def deleteBack(self):
        """ 
        :type head : Node
        """
        if self.head:
            curr = self.head
            while curr.next:
                curr=curr.next
            curr = None
            
    #deletes Node loc; returns head
    def deleteNode(self, loc):
        """ 
        :type self : Node
        :type loc : Node
        :rtype : Node
        """
        if self.head:
            curr = self.head
            while curr.next:
                curr=curr.next
                if curr.next == loc:
                    temp = curr.next.next
                    curr.next = None
                    curr.next = temp
        return self.head
    
    #returns length of the list
    def length(self):
        """ 
        :type head : Node
        :rtype : Int
        """
        length = 0
        if self.head:
            length+=1
            while curr.next:
                length+=1
                curr=curr.next
        return length

    # reverses the linked list iteratively
    def reverseIterative(self):
        """ 
        :type head : Node
        """
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    def reverseRecursiveHelper(self, head):
        """ 
        :type head : Node
        """       
        if self is None or self.next is None:
            return self
        rest = self.reverseRecursiveHelper(head.next)
        
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest

    #reverses the linked list recursively (Hint: you will need a helper function)
    def reverseRecursive(self):
        """ 
        :type head : Node
        """
        reverseRecursiveHelper(self, self.head)

        
        return
"""
"""