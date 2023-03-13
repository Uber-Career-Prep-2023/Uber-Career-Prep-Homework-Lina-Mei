"""
Question 3: ZeroSumSubArrays

Given an array of integers, count the number of subarrays that sum to zero.

Time complexity: o(n^2)
Space complexity: o(n)


"""    
def ZeroSumSubArrays(arr):
    """
    :type arr : List[int]
    :rtype int
    """
    count = 0
    i = 0
    while (i < len(arr)) :
        prefix = 0
        j = i
        while (j < len(arr)) :
            prefix += arr[j]
            if (prefix == 0) :
                count += 1
            j += 1
        i += 1
    return count


arr = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(ZeroSumSubArrays(arr))

arr = [1, 8, 7, 3, 11, 9]
print(ZeroSumSubArrays(arr))

arr = [8, -5, 0, -2, 3, -4]
print(ZeroSumSubArrays(arr))
""" 
    Examples:
    Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
    Output: 2
    (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

    Input Array: [1, 8, 7, 3, 11, 9]
    Output: 0

    Input Array: [8, -5, 0, -2, 3, -4]
    Output: 2
    (Subarrays: [0], [8, -5, 0, -2, 3, -4])
"""

# Spent 35 minutes
# wasn't sure how to improve the time complexity