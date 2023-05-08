""" 
Copy-paste your implementation from Question 1 and modify it. Your Node struct should have an additional prev reference as well as a next.

Time Complexity:
Space Complexity:


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # creates new Node with data val at front; returns new head 
    def insertAtFront(self, val):
        """ 
        :type self : Node
        :type val : int
        :rtype : Node
        """
        if self.head is None:
            self.head = Node(val)
            return
        x = Node(val)
        x.next = self.head
        self.head = x
        curr = self.head.next
        curr.prev = self.head
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
            prev = None
            curr = self.head
            while curr.next:
                prev = curr
                curr=curr.next
            curr.next = Node(val)
            curr.prev = prev
        
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
            prev = None
            curr = self.head
            while curr.next:
                prev = curr
                if curr.next == loc:
                    temp = curr.next.next
                    temp.prev = curr
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
                self.prev = None
            else:
                self.next.prev = None
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
                    temp.prev = curr
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
        :type self : Node
        """
        temp = None
        current = self.head
        while(current):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
            
        if temp is not None:
            self.head = temp.prev
        
    def reverseRecursive(self):       
        head = self.head
        if not head:
            return None
    
        temp = head.next
        head.next = head.prev
        head.prev = temp
    
        if not head.prev:
            return head
    
        return head.prev.reverseRecursive()

    # Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                                str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

def main():
    # Start with the empty list
    list = DoublyLinkedList()
    list.insertAtFront(2)
    list.insertAtFront(4)
    list.insertAtFront(8)
    list.insertAtFront(10)
    print(list)
    list.reverseIterative()
    print(list)
    list.reverseRecursive()
    print(list)

main()

