""" 
Given a singly linked list, disconnect the cycle, if one exists.

Time Complexity: O(N)
Space Complexity: O(1)

20 minutes total

Explanation:
    The time complexity is O(N) where N represents the number of elements in the linked list because there are two pointers,
    one fast and slow. The fast pointer will traverse through the linked list twice as the worse case scenario.
    
    The space complexity is O(1) because we are just using 2 variables which requires constant space.

"""
from SinglyLinkedList import *

def DisconnectCycle(list: SinglyLinkedList):
    turtle = list.head
    chicken =  turtle.next
    while chicken.next:
        if chicken.next == None:
            return False
        if turtle == chicken.next:
            chicken.next = None
            return
        chicken = chicken.next.next
        turtle = turtle.next
    return


def main():
    list = SinglyLinkedList()
    cycle = Node(4)
    repeated = Node(12)
    cycle.next = repeated
    list.head = cycle
    list.insertAtFront(11)
    list.insertAtFront(9)
    repeated.next = list.head
    list.head = repeated
    list.insertAtFront(18)
    list.insertAtFront(10)

    DisconnectCycle(list)
    print(list) # 10 18 12 9 11 4
    
    list2 = SinglyLinkedList()
    cycle = Node(4)
    cycle.next = cycle
    list2.head = cycle
    list2.insertAtFront(11)
    list2.insertAtFront(9)
    list2.insertAtFront(12)
    list2.insertAtFront(18)
    list2.insertAtFront(10)    
    DisconnectCycle(list2)
    print(list2) # 10 18 12 9 11 4   
    return

main()