""" 
Given a doubly linked list, determine if it is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)

13 minutes Total

Explanation:
    The time complexity is O(n) where n is the number of elements in the linked list.
    We have a while loop when we have to reach the end of the linked list and we have another while loop to traverse to the middle which
    runs in linear time
    
    The space complexity is O(1) because it uses a constant amount of extra space regardless of the input size.
"""

from DoublyLinkedList import *

def IsPalindrome(doublylinkedlist: DoublyLinkedList):
    
    tail = curr = doublylinkedlist.head
    
    while tail.next:
        tail = tail.next
        
    while curr:
        if curr.data != tail.data:
            return False
        if curr.next == tail.prev: # middle point / intersecting point
            return True
        curr = curr.next
        tail = tail.prev
        
    return True

def main():
    
    list = DoublyLinkedList()
    list.insertAtFront(9)
    list.insertAtFront(2)
    list.insertAtFront(4)
    list.insertAtFront(2)
    list.insertAtFront(9)
    print(list) # 9 2 4 2 9
    print(str(IsPalindrome(list))) # true
    
    list2 = DoublyLinkedList()
    list2.insertAtFront(9)
    list2.insertAtFront(2)
    list2.insertAtFront(4)
    list2.insertAtFront(12)
    list2.insertAtFront(9)
    
    print(list2) # 9 12 4 2 9
    print(str(IsPalindrome(list2))) # false

    return
main()