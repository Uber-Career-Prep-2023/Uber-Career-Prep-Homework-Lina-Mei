"""
Question 10: TwoSum

Given an array of integers and a target integer, k, return the number of pairs of integers in the array 
that sum to k. In each pair, the two items must be distinct elements (come from different indices in the array).


Time complexity: 
Space complexity:
# 

"""

def TwoSum(arr, k):
    """ 
    :type arr : List[int]
    :rtype int
    """
    # iterate through arr
    # create hash map, map the current index to (k-current index)
    # check if current index is a value in the hash map, if it is, then a pair has been created
    map = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] in map.values():
            count+=1
        else:
            target = k - arr[i]
            map[arr[i]]=target
            print(map)
    return count

arr=[1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
k=10
print(TwoSum(arr,k))

arr=[1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
k=8
print(TwoSum(arr,k))

arr=[4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
k=6
print(TwoSum(arr,k))

arr=[4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
k=1
print(TwoSum(arr,k))
""" 
Examples:

Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Input k: 10
Output: 3
(Pairs: (8, 2), (8, 2), (3, 7))

Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Input k: 8
Output: 4
(Pairs: (10, -2), (3, 5), (1, 7))

Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Input k: 6
Output: 5
(Pairs: (4, 2), (0, 6), (3, 3), (3, 3), (3, 3))

Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Input k: 1

"""


# confused about test case #2, there are 3 pairs in the example but the output is 4?
# also confused about test case #3, why doesn't it output 6? Since there are two 3's
# common mistakes : keep forgetting the () such as in map.values()
# Spent 15 minutes