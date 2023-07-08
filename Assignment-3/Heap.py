""" 
Write a min heap class according to the following API using an array as the underlying data structure. 
(A max heap has the same implementation; you simply need to flip the direction of the comparators.) 
For simplicity, you can assume that the heap holds integers rather than generic comparables.

Time complexities:
look up - o(1), retrieve top element is quick
insertion - o(logn), heaps are split into 2, where left is smaller and right is bigger
remove - o(logn), with every traversal to find the node to remove, 
                you are dividing the # of elements to search through by 2, therefore half the work
create - o(nlogn), same reason as above

Space complexity:
create - o(n) where n is number of elements
"""
class Heap:
    arr = []
    
    def __init__(self):
        self.arr = []

    def parent(self, pos):
        return pos//2
  
    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1
    
    def top(self):
        return self.arr[0]
    
    def maxsize(self):
        return len(self.arr)
    
    def insert(self, x):
        self.arr.append(x)
        self.heapify(len(self.arr) - 1)
            
    def swap(self, first, second):
        if first >= len(self.nodes) or second >= len(self.nodes):
            return
        tmp = self.arr[first]
        self.arr[first] = self.noarrdes[second]
        self.arr[second] = tmp
        
    def heapify(self, index):
        if not index:
            index = len(self.arr) - 1
        parent = self.parent(index)
        if self.parent(index) and self.arr[index] < self.parent(index):
            self.swap(index, parent)
            self.heapify(index=parent)
        return self.arr
        
    def heapifyDown(self, index):
        if index >= len(self.arr) or not self.leftChild(index):
            return index
        smallerChild = self.leftChild(index)
        if self.rightChild(index) and self.rightChild(index) < smallerChild:
            smallerChild = self.rightChild
        if self.arr[index] < self.arr[smallerChild]:
            return index
        if self.arr[index] > self.arr[smallerChild]:
            self.swap(index, smallerChild)
            return self.heapifyDown(smallerChild)
        
        
    def remove(self):
        if len(self.arr) <= 0:
            return None
        popped = self.arr[0]
        self.arr[0] = self.arr[len(self.arr)-1]
        del self.arr[-1]
        self.heapifyDown(self.arr[0])
        return popped

def main():
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(10)
    heap.insert(5)
    print(heap.top())
    heap.remove()
    print(heap.top())
    
    print(heap.arr[0])
    print(heap.arr[1])
    print(heap.arr[2])


main()