""" 
Implement the following methods. Rather than having a separate linked list class, 
we will pass a Node struct that represents the head of the list (this is common practice in interview questions). 
The linked list article includes a Node struct definition in a number of common languages (C++, Python, Java, JavaScript); 
feel free to use it in your implementation. For simplicity, you can make your nodes store integers rather than generic data types.
In each of the methods, you should use pointers in languages that support pointers (e.g., Node * in C++) or a reference in languages 
that support references (e.g., Python).

Time Complexity: O(N) where N is the length of the list because it needs to visit each node once
Space Complexity: O(N) because of the recursive call 

~1.5 hour taken total

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
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
        if self.head is None:
            self.head = None
            
        curr = self.head
        while curr.next.next:
            curr = curr.next
        node_deleted = curr.next
        curr.next = None
        
            
    #deletes Node loc; returns head
    def deleteNode(self, loc: Node):
        """ 
        :type self : SinglyLinkedList
        :type loc : Node
        :rtype : Node
        """
        curr = self.head        
        if curr is None:
            return None
        if curr == loc:
            self.head = curr.next
            return self.head
        
        while (curr):
            if curr.next == loc:
                if curr.next.next:
                    temp = curr.next.next
                    curr.next = temp
                    break
                else:
                    curr.next = None
            curr = curr.next
        return self.head
    
    #returns length of the list
    def length(self):
        """ 
        :type head : Node
        :rtype : Int
        """
        length = 0
        curr = self.head
        while curr:
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


    #reverses the linked list recursively (Hint: you will need a helper function)
    def reverseRecursive(self: Node):
        def reverse_helper(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverse_helper(next_node, curr)
        
        self.head = reverse_helper(self.head, None)
    
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
    ll = SinglyLinkedList()
    ll.insertAtFront(1)
    ll.insertAtFront(2)
    print(ll.length()) # 2
    ll.deleteBack()
    print(ll.length()) # 1
    print(ll.head.data) # 2
    
    ll.insertAtFront(3)
    ll.insertAtFront(4)
    ll.insertAtFront(5) 
    ll.reverseIterative() 
    print(ll) # 2 3 4 5
    ll.reverseRecursive()
    print(ll) # 5 4 3 2
    print("ran SinglyLinkedList.py")

main()