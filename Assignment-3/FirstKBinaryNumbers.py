""" 
Given a number, k, return an array of the first k binary numbers, represented as strings.

30 minutes Total
Time complexity: O(n*logn)
Space complexity: O(n)

Explanation: 
O(klog(k)) time complexity because the outer loop runs k times, while the inner loops perform division which will be log(k) time. 
O(k) space complexity because we have to store k number of elements in the output array

Data Structure: Array
Algorithm: N/a

Assumptions: That k is non-negative
"""

def firstKBinaryNumbers(k):
    binary_numbers = []
    for i in range(k):
        binary = ""
        num = i
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
        binary_numbers.append(binary if binary != "" else "0")
    return binary_numbers

def main():
    num = 5
    print(firstKBinaryNumbers(num)) # ["0", "1", "10", "11", "100"]
    num2 = 10
    print(firstKBinaryNumbers(num2)) # "0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
    return
main()