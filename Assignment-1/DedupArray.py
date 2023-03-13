"""
Question 9: DedupArray

Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. 
If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the 
left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

Time complexity: O(n)
Space complexity: O(1)

Assuming that array will not be empty
Assuming that I'm allowed to use built-in functions
"""

def DedupArray(arr):
    """ 
    :type arr : List[int]
    :rtype List[int]
    """
    # traverse through arr
    # add to set
    # convert set to list
    set = {arr[0]}
    for i in range(len(arr)):
        set.add(arr[i])
    return list(set)


arr=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(DedupArray(arr))

arr=[0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
print(DedupArray(arr))

arr=[1, 3, 4, 8, 10, 12]
print(DedupArray(arr))

""" 
Examples:
Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Modified Array: [1, 2, 3, 4] 
or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
or [1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

Input Array: [1, 3, 4, 8, 10, 12]
Modified Array: [1, 3, 4, 8, 10, 12]

"""

# Spent 10 minutes

# hate how set = {} will indicate an empty dict, wonder how we can go around this?