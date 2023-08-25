'''
The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!. 
Given a non-negative integer n, return the Catalan numbers 0-n.

Examples:
Input: 1
Output: 1, 1

Input: 5
Output: 1, 1, 2, 5, 14, 42

Approach: DP
Time complexity: O(n^2) because recursion is used and in the worst case, 
it needs to compute the factorial of every number from 1 to 2n
Space complexity: O(n) because the result arr will store n+1 catalan numbers
Time taken: 20 minutes

'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
def catalan(num):
    result = []
    for i in range(num+1):
        top = factorial(2*i)
        bottom = factorial(i+1) * factorial(i)
        result.append(top/bottom)
    return result

print(catalan(1)) # Output: 1, 1
print(catalan(5)) # Output: 1, 1, 2, 5, 14, 42

