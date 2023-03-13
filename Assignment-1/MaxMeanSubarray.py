"""
Question 1: MaxMeanSubarray
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Time complexity: O(n)
Space complexity: O(1
assume that there are no empty arrays
assume that k will always be less than the size of the given array
"""

def MaxMeanSubArray(nums, k):
    """
    :type nums : List[int]
    :type k : size k integer
    :rtype float
    """
    left = 0
    if (len(nums) == 0):
        print("empty nums")
        return 0
    best = -99999
    temp = -9999
    for i in range(len(nums)-1):
        #if left + right > best, replace best, move right pointer
        average = (nums[left] + nums[i])/2
        if (average > best):
            if (i-left <= k):
                best = average
        #else move left pointer
        else:
            left += 1
    print(best)
 
nums = [4, 5, -3, 2, 6, 1]
k = 2
MaxMeanSubArray(nums, k)

nums2 = [4, 5, -3, 2, 6, 1]
k2 = 3
MaxMeanSubArray(nums2, k2)

nums3 = [1, 1, 1, 1, -1, -1, 2, -1, -1]
k3 = 3
MaxMeanSubArray(nums3, k3)

nums4 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k4 = 5
MaxMeanSubArray(nums4, k4)

"""
Examples:
Input Array: [4, 5, -3, 2, 6, 1]
Input k = 2
Output: 4.5

Input Array: [4, 5, -3, 2, 6, 1]
Input k = 3
Output: 3

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1]
Input k = 3
Output: 1

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
Input k = 5
Output: 1
"""

# Spent 20-25 minutes