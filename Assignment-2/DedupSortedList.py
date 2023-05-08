from SinglyLinkedList import *

""" 
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Time Complexity: O(N) where N represents the number of elements in the tree
Space Complexity: O(N) 

10 minutes taken total

Explanation:
    The time complexity is O(N) because we have to traverse through all the nodes in the tree to remove duplicates
    The space complexity is O(1) because we do not need new space allocation at all. We create a variable at most which runs at constant time.
"""

def DedupSortedList(list):
    curr = list.head
    while curr.next:
        if curr.next.data == curr.data:
            temp = curr.next.next
            list.deleteNode(curr.next)
            curr.next = temp
        else:
            curr = curr.next
    return list

def main():
    list = SinglyLinkedList()
    list.insertAtBack(1)
    list.insertAtBack(2)
    list.insertAtBack(2)
    list.insertAtBack(4)
    list.insertAtBack(5)
    list.insertAtBack(5)
    list.insertAtBack(5)
    list.insertAtBack(10)
    list.insertAtBack(10)

    print(list)
    DedupSortedList(list)
    print(list)
    
    list2 = SinglyLinkedList()
    list2.insertAtBack(8)
    list2.insertAtBack(8)  
    list2.insertAtBack(8)  
    list2.insertAtBack(8)
    DedupSortedList(list2)  
    print(list2)  
    
    return
main()