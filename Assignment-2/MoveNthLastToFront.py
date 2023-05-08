""" 
Given a singly linked list, move the nth from the last element to the front of the list.


Time Complexity: O(N)
Space Complexity: O(1)

25 minutes taken total

Explanation:
    The time complexity is O(n) because worst case scenario, we have to traverse to the end of the list to get the last element of the list.
    The space complexity is O(1) because we are only using variables which runs at constant time.
"""

from SinglyLinkedList import *

def MoveNthLastToFront(list: SinglyLinkedList, n: int):
    curr = list.head
    length = list.length()
    
    if n > length or curr is None:
        return curr
    
    target = length - n + 1
    count = 1
    node = None
    while curr:
        if count == target:
            node = curr
            list.deleteNode(curr)
            break
        else:
            count+=1
            curr = curr.next
            
    list.insertAtFront(node.data)
    return list

from copy import deepcopy # for testing purposes

def main():
    list = SinglyLinkedList()
    list.insertAtFront(19)
    list.insertAtFront(6)
    list.insertAtFront(11)
    list.insertAtFront(9)
    list.insertAtFront(20)
    list.insertAtFront(7)
    list.insertAtFront(8)
    list.insertAtFront(2)
    list.insertAtFront(15)
    print(list) # 15 2 8 7 20 9 11 6 19

    list2 = deepcopy(list)
    MoveNthLastToFront(list, 2)
    print(list) # 6 16 2 8 7 20 9 11 19
    
    print(list2) # 15 2 8 7 20 9 11 6 19
    MoveNthLastToFront(list2, 7)
    print(list2) # 8 15 2 7 20 9 11 6 19

    
    return
main() 