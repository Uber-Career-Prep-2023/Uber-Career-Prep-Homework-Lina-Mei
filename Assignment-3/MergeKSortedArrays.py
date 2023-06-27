"""
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

Time Complexity: O(klogn) because insertion is logn for heaps and there are k arrays
Space Complexity: O(n) where n is the number of the sum of the size of all arrays
Data Structure: Heap
Algorithm: 
Time Taken: 25 minutes

"""
import heapq

def merge(k, arrays):
    # put everything in 1 heap, use min to retrieve minimum number
    heap = []
    ret = []
    for array in arrays:
        for i in array:
            heapq.heappush(heap, i) # push all numbers to curr
    
    while heap:
        min = heapq.heappop(heap) # pop smallest val and add to res
        ret.append(min)
    return ret

def main():
    arr = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print(merge(2, arr)) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    arr2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print(merge(3, arr2)) # Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
    return

main()