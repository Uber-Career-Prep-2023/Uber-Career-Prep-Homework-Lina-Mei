from SinglyLinkedList import *
from DoublyLinkedList import *

""" 
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Time Complexity:
Space Complexity:

"""

def DedupSortedList(list):
    curr = list.head
    set = {curr.data}
    curr = curr.next
    while curr:
        if curr.data in set:
            list.deleteNode(curr)
        else:
            set.add(curr.data)
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
    
    return
main()