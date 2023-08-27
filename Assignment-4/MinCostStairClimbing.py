'''
A staircase on a hiking trail implements a rather unusual toll system to cover trail maintenance costs. 
Each stair in the staircase has a different toll which you only have to pay if you step on that stair. 
Due to the height of the stairs, you can only climb one or two stairs at once. 
This means that from the ground you must initially step on either stair 0 or stair 1 and that, 
if there are n stairs, the last stair you step on can be either stair n-1 or n-2. 
Given an array representing the costs per stair, what is the minimum possible toll you can pay to climb the staircase?

Examples:
Input: [4, 1, 6, 3, 5, 8]
Output: 9 (step on stairs 1, 3, 4 for a cost of 1+3+5)

Input: [11, 8, 3, 4, 9, 13, 10]
Output: 25 (step on stairs 1, 3, 5 for a cost of 8+4+13)

Approach: dp
Time complexity: O(N), N represents the # of elements in the given input array. We will traverse at most
every element in the given array once.
Space complexity: O(N), N represents the # of elements in the given input array. We will store the min cost possible starting 
from step 0 or step 1 for every element for the array
Time taken: 20 minutes

'''

def minCostStairClimbing(arr):
    dp = [0]*len(arr)
    
    # cost at dp[0] will always equal to the cost of arr[0] and dp[1] = cost of arr[1]
    dp[0] = arr[0]
    dp[1] = arr[1]
    
    # the best current cost at each element in the array will be arr[i] + min(cost of 1 stair before or 2 stairs before)
    for i in range(2, len(arr)):
        dp[i] = arr[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1],dp[-2])

input = [4, 1, 6, 3, 5, 8]
print(minCostStairClimbing(input)) #9

input2 = [11, 8, 3, 4, 9, 13, 10]
print(minCostStairClimbing(input2)) #25

    
    
    