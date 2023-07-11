"""
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

Time Complexity: 
    O(klogk) where because we have to retrieve the first element of the array at least once 
    and we also have to insert the element into the heap which runs at log(k) time
Space Complexity: 
    O(k) where k is the number of arrays because we always start with the first element of 
    every array in the arrays and we always pop and add 1 more element at a time
Data Structure: Heap
Algorithm: Merge
Time Taken: 40 minutes

"""
import heapq

def merge(k, arrays):
    ret = []
    heap = []
    heapq.heapify(heap)

    # iterate through all array in arrays
    for i in range(len(arrays)):
        # heap of size k
        # add to heap a tuple of (value, array #, array index position)
        heapq.heappush(heap, (arrays[i][0], i, 0))
    while(len(heap) > 0):
        value, arr_num, arr_index = heapq.heappop(heap)
        ret.append(value)
        # if the array has no more elements, we can just move on to the next smallest ele in heap
        if arr_index+1 < len(arrays[arr_num]):
            to_insert = (arrays[arr_num][arr_index+1],arr_num,arr_index+1)
            heapq.heappush(heap, to_insert)
    return ret

def main():
    arr = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print(merge(2, arr)) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    arr2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print(merge(3, arr2)) # Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
    arr3 = [[1, 1, 1, 1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print(merge(2, arr3)) # Output: [1, 1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    return

main()