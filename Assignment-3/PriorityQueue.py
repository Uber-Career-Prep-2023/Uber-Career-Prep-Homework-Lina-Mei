""" 
A priority queue functions like a queue except that elements are 
removed in order of priority rather than insertion. This is typically
implemented as a max heap that stores pairs of elements and numeric 
weights, with the weights used as the values in the heap. Implement 
a priority queue according to the following API using a heap as the 
underlying data structure. For simplicity, you can assume the priority 
queue stores string elements with integer priorities. Start by copy-pasting 
your heap implementation from question 2 and making modifications.


"""
class PriorityQueue:
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
    
    def insert(self, x, weight):
        self.arr.append(x, weight)
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
    heap = PriorityQueue()
    heap.insert('a', 5)
    heap.insert('b', 3)
    heap.insert('c', 1)
    heap.insert('d', 5)
    heap.insert('e', 3)
    print(heap.top())
    heap.remove()
    print(heap.top())
    
    print(heap.arr[0])
    print(heap.arr[1])
    print(heap.arr[2])

main()