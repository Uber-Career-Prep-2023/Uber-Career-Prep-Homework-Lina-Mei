""" 
Copy-paste your implementation from Question 1 and modify it. Your Node struct should have an additional prev reference as well as a next.

Time Complexity: O(N) where N is the length of the list because it needs to visit each node once
Space Complexity: O(N) because of the recursive call

~1.5 hour taken total

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
            
    def reverse_helper(node: Node) -> Node:
        if not node or not node.next:
            return node
        
        next_node = node.next
        new_head = reverse_helper(next_node)
        
        next_node.next = node
        node.prev = next_node
        node.next = None
        
        return new_head    
    
    def reverseRecursive(head: Node) -> Node:
        if not head or not head.next:
            return head
        
        new_head = reverse_helper(head)
        new_head.prev = None
        return new_head
        

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
    list.reverseRecursive(list.head)
    print(list)

main()

