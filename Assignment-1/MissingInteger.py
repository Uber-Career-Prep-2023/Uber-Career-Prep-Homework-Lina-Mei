"""
Question 6: MissingInteger
Given an integer n and a sorted array of integers of size n-1 which contains all but 
one of the integers in the range 1-n, find the missing integer.

Time complexity: O(n)
Space complexity: O(1)
Assuming that num will always be greater than the size of arr
Assuming that num will always start at 1
"""
def MissingInteger(arr, num):
    # set temp = 1
    # traverse through arr and doing count++, if count != arr, return count
    temp = 1
    for i in range(len(arr)):
        if temp != arr[i]:
            return temp
        else:
            temp += 1
    return num
        
            

arr = [1, 2, 3, 4, 6, 7]
num = 7
print(MissingInteger(arr, num))

arr = [1]
num = 2
print(MissingInteger(arr, num))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
num = 12
print(MissingInteger(arr, num))

""" 
Examples:
Input Array: [1, 2, 3, 4, 6, 7]
Input n: 7
Output: 5

Input Array: [1]
Input n: 2
Output: 2

Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
Input n: 12
Output: 9
"""

# spent 17 minutes, i wasn't sure how to account for array of size 1 (second test case)