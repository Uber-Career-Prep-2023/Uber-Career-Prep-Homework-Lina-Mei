"""
Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

Time Complexity: O(N) where N represents the number of elements in the tree
Space Complexity: O(m) where m represents the maximum number of elements in each level of the tree

40 minutes Taken (nothing was wrong with my implementation, but I incorrectly wrote my test cases)

Explanation:
    The time complexity is O(N) because we have to traverse through all the nodes in the tree and add it into the queue
    which runs at linear time.
    
    The space complexity is O(m) because the queue is as big as the maximum number of nodes in each level.

"""

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def LeftView(root: Node):
    if not root:
        return []
    arr = []
    queue = deque()
    queue.append(root)
    while(queue):
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                arr.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return arr

def main():
    n7 = Node(7)
    n3 = Node(3)
    n9 = Node(9)
    n20 = Node(20)
    n14 = Node(14)
    n13 = Node(13)
    
    n14.right = Node(15)
    n13.right = n14
    n3.right= n13
    n3.left = n9
    n9.left = n20
    n7.left = Node(8)
    n7.right = n3

    arr = LeftView(n7) # [7, 8, 9, 20, 15]
    print(arr)

    n4 = Node(4)
    n8 = Node(8)
    n20 = Node(20)
    n15 = Node(15)
    n6 = Node(6)
    n11 = Node(11)
    
    n7.left = n20
    n7.right = n4
    n20.left = n15
    n20.right = n6    
    n4.left = n8
    n4.right = n11
    arr2 = LeftView(n7) # [7, 20, 15]
    print(arr2)

            

main()